from django.db import models
from django.utils.translation import ugettext_lazy as _
from profiles.models import ClassGroup
import datetime

class Cursus(models.Model):
    """A cursus can be "Master of Science 2011", it's just like a promotion

    """
    name = models.CharField(blank=False, max_length=150)
    start_date = models.DateField(default=datetime.datetime.today)
    manager = models.ForeignKey('profiles.Profile', related_name="cursus_managed")
    
    @property
    def classgroup_set(self):
        """Return the classgroup that are foloowing the active cursus"""
        return ClassGroup.objects.filter(cursus=self)
    
    def __unicode__(self):
        return self.name

class StudyPeriod(models.Model):
    name = models.CharField(blank=False, max_length=150, help_text=_("ex. Semester 1, Trimester 2, etc."))
    cursus = models.ForeignKey('Cursus')
    start_date = models.DateField(default=datetime.datetime.today)
    end_date = models.DateField()
    
    @property
    def manager(self):
        """Returns the manger of the cursus"""
        return self.cursus.manager

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(blank=False, max_length=150)
    study_period = models.ForeignKey('StudyPeriod')
    panned_hours = models.PositiveIntegerField(blank=False, null=False)

    @property
    def manager(self):
        """Returns the manger of the cursus"""
        return self.study_period.manager


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
    planned_hours = models.IntegerField()
    subject = models.ForeignKey('Subject', related_name="modalities" )
    type = models.CharField(blank=False, max_length=100, choices=TYPE_CHOICES)

    @property
    def manager(self):
        """Returns the manger of the cursus"""
        return self.subject.manager
    
    @property
    def classgroup_set(self):
        """Returns a nice name"""
        return ClassGroup.objects.filter(cursus=self)
    
    def __unicode__(self):
        return dict(self.TYPE_CHOICES)[self.type]
