from django.db import models
from django.utils.translation import ugettext_lazy as _
from profiles.models import ClassGroup
from managers import CampusManager, PlaceManager

class Campus(models.Model):
    name = models.CharField(blank=False, max_length=150)
    university = models.ForeignKey('University')
    manager = models.ForeignKey('profiles.Profile', 
        related_name="campus_managed", blank=True, null=True) 
    objects = CampusManager()

    @property
    def address(self):
        """return the address, if specified somewhere"""
        try:
            place = Place.objects.get(campus=self, is_main_place=True) 
            return place.address
        except Place.DoesNotExists:
            return None

    def classgroup_set(self):
        return ClassGroup.objects.filter(campus=self)

    def __unicode__(self):
        return self.name

class University(models.Model):
    name = models.CharField(blank=False, max_length=150, 
                            help_text=_("University full name"))
    
    def __unicode__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(blank=False, max_length=150)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    campus = models.ForeignKey('Campus')
    address = models.CharField(blank=True, max_length=500)
    is_main_place = models.BooleanField(default=False)
    
    objects = PlaceManager()

    @property
    def manager(self):
        """Returns the manager of the campus"""
        return self.campus.manager

    
    def __unicode__(self):
        return self.name
