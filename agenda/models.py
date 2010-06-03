"""Models for the agenda application. Here lives all the data related logic of
EasyTimeTable.

All logic is contained here, and not in views, because it makes it simpler to
maintain afterwards.

"""
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from managers import *

# -- Event related models ----------------------------------------------------

class When(models.Model):
    date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    event = models.ForeignKey('Event')
    objects = WhenManager()
    
    def __unicode__(self):
        return self.date.strftime('%d-%B-%Y')
    
    def to_fullcalendar_dict(self, is_editable=lambda when:False,
    css_class='undef'):
        """Return this object under a FullCalendar compatible dict format.

        The is_editable callable is called with the 

        """
        dct = { 'title' : self.event.name,
                'id' : self.id,
                'event_id': self.event_id,
                'allDay' : False,
                'start' : self.date.isoformat(),
                'end' : (self.date +
                datetime.timedelta(hours=self.event.duration)).isoformat(),
                'editable' : is_editable(self),
                'className' : css_class,
            }
        return dct

class Who(models.Model):
    """The Who model has some references to different others models.

    To know who is concerned by an event, it have a method that return this
    informations.
    """
    event = models.ForeignKey('Event')
    user = models.ForeignKey(User, null=True, blank=True)
    classgroup = models.ForeignKey('ClassGroup', null=True, blank=True)
    cursus = models.ForeignKey('Cursus', null=True, blank=True)
    campus = models.ForeignKey('Campus', null=True, blank=True)
    university = models.ForeignKey('University', null=True, blank=True)

    # set to true if it concerns everyone.
    is_universal = models.BooleanField(default=False)

class Event(models.Model):
    name = models.CharField(blank=False, max_length=150)
    duration = models.PositiveIntegerField(blank=False, null=False)
    places = models.ManyToManyField('Place', null=True, blank=True)
    subject_modality = models.ForeignKey('SubjectModality', null=True,
    blank=True)
    force_display = models.BooleanField(default=False)
    place_text = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.name

# -- localisation models ------------------------------------------------------

class Campus(models.Model):
    name = models.CharField(blank=False, max_length=150)
    university = models.ForeignKey('University')
    
    def __unicode__(self):
        return self.name

class University(models.Model):
    name = models.CharField(blank=False, max_length=150, help_text=_("University full name"))
    
    def __unicode__(self):
        return self.name

class ClassGroup(models.Model):
    name = models.CharField(blank=False, max_length=150)
    campus = models.ForeignKey('Campus')
    cursus = models.ForeignKey('Cursus')

    def __unicode__(self):
        return self.name
    

class Place(models.Model):
    name = models.CharField(blank=False, max_length=150)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    campus = models.ForeignKey('Campus')
    address = models.CharField(blank=True, max_length=500)
    is_main_place = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name

# -- pedagogy models ----------------------------------------------------------

class Cursus(models.Model):
    """A cursus can be Master of Science 2011, it's just like a promotion

    """
    name = models.CharField(blank=False, max_length=150)
    start_date = models.DateField(default=datetime.datetime.today)
    
    def __unicode__(self):
        return self.name

class StudyPeriod(models.Model):
    name = models.CharField(blank=False, max_length=150, help_text=_("ex. Semester 1, Trimester 2, etc."))
    cursus = models.ForeignKey('Cursus')
    start_date = models.DateField(default=datetime.datetime.today)
    end_date = models.DateField()
    
    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(blank=False, max_length=150)
    study_period = models.ForeignKey('StudyPeriod')
    panned_hours = models.PositiveIntegerField(blank=False, null=False)

    def __unicode__(self):
        return self.name

class SubjectModality(models.Model):
    TYPE_CHOICES = (
        ('presential', 'Presential'),
        ('elearning', 'E-learning'),
        ('tp', 'TP'),
        ('theorical_evaluation', 'Theorical Evaluation'),
        ('practical_evaluation', 'Practical Evaluation'),
        ('soutenance', 'Soutenance'),
    )
    planned_hours = models.DecimalField(max_digits=4, decimal_places=2)
    subject = models.ForeignKey('Subject')
    type = models.CharField(blank=False, max_length=100, choices=TYPE_CHOICES)

    def __unicode__(self):
        return dict(self.TYPE_CHOICES)[self.type]

# -- other models -------------------------------------------------------------

class Profile(models.Model):
    """A user profile. Can be useful for students, to define classgroups."""
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(blank=False, max_length=150)
    last_name = models.CharField(blank=False, max_length=150)
    birth_date = models.DateField(default=datetime.datetime.today)
    classgroup = models.ForeignKey('ClassGroup', null=True, blank=True)
