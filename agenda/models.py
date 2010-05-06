from django.db import models
from django.contrib.auth.models import User
import datetime


# TODO Add managers

class When(models.Model):
    """Reprensents the "when" of an event. 

    """
    date = models.DateTimeField(blank=True, default=datetime.datetime.now)    
    event = models.ForeignKey('Event')
    
    def __unicode__(self):
        return u"When"

class Campus(models.Model):
    name = models.CharField(blank=False, max_length=150)
    university = models.ForeignKey('University')
    
    def __unicode__(self):
        return u"Campus"

class University(models.Model):
    name = models.CharField(blank=False, max_length=150)
    
    def __unicode__(self):
        return self.name

class ClassGroup(models.Model):
    name = models.CharField(blank=False, max_length=150)    
    campus = models.ForeignKey('Campus')
    cursus = models.ForeignKey('Cursus')

    def __unicode__(self):
        return self.name
    
class Who(models.Model):
    """The Who model has some references to different others models.

    To know who is concerned by an event, it have a method that return this
    informations.
    """
    user = models.ForeignKey(User)
    classgroup = models.ForeignKey(ClassGroup)
    cursus = models.ForeignKey('Cursus')
    campus = models.ForeignKey(Campus)
    event = models.ForeignKey('Event')
    university = models.ForeignKey('University')
    is_universal = models.BooleanField(default=False)

    def __unicode__(self):
        return u"Who"

class Place(models.Model):
    name = models.CharField(blank=False, max_length=150)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    campus = models.ForeignKey('Campus')
    address = models.CharField(blank=True, max_length=500)
    is_main_place = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name

class Cursus(models.Model):
    """A cursus can be Master of Science 2011, it's just like a promotion

    """
    name = models.CharField(blank=False, max_length=150)
    start_date = models.DateField(default=datetime.datetime.today)
    
    def __unicode__(self):
        return self.name

class StudyPeriod(models.Model):
    name = models.CharField(blank=False, max_length=150)
    cursus = models.ForeignKey('Cursus')
    start_date = models.DateField(default=datetime.datetime.today)
    end_date = models.DateField()
    
    def __unicode__(self):
        return u"StudyPeriod"


class Subject(models.Model):
    name = models.CharField(blank=False, max_length=150)
    study_period = models.ForeignKey(StudyPeriod)
    panned_hours = models.PositiveIntegerField(blank=False, null=False)
    
    def __unicode__(self):
        return self.name

class SubjectModality(models.Model):
    TYPE_CHOICES = (
        ('presential', 'Presential'),
        ('elearning', 'E-learning'),
        ('tp', 'TP'),
        ('theorical_valuation', 'Theorical Evaluation'),
        ('practical_evaluation', 'Practical Evaluation'),
        ('soutenance', 'Soutenance'),
    )
    planned_hours = models.DecimalField(max_digits=4, decimal_places=2)
    subject = models.ForeignKey('Subject')
    type = models.CharField(blank=False, max_length=100, choices=TYPE_CHOICES)

    def __unicode__(self):
        return u"SubjectModality"

class Event(models.Model):
    name = models.CharField(blank=False, max_length=150)
    duration = models.PositiveIntegerField(blank=False, null=False)
    places = models.ManyToManyField(Place, null=True)
    subject_modality = models.ForeignKey(SubjectModality)
    force_display = models.BooleanField(default=False)
    place_text = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.name

class Profile(models.Model):
    """A user profile. Can be useful for students, to define classgroups."""
    user = models.ForeignKey(User, unique=True)
    classgroup = models.ForeignKey(ClassGroup, null=True)
