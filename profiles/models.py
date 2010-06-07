from django.db import models
from django.contrib.auth.models import User
import datetime

from managers import ClassGroupManager

class Profile(models.Model):
    """A user profile. Can be useful for students, to define classgroups."""
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(blank=False, max_length=150)
    last_name = models.CharField(blank=False, max_length=150)
    birth_date = models.DateField(default=datetime.datetime.today)
    classgroup = models.ForeignKey('ClassGroup', null=True, blank=True)
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class ClassGroup(models.Model):
    name = models.CharField(blank=False, max_length=150)
    campus = models.ForeignKey('locations.Campus', related_name="class_group")
    cursus = models.ForeignKey('pedagogy.Cursus', related_name="class_group")
    manager = models.ForeignKey('Profile', related_name="class_group_managed")
    
    objects = ClassGroupManager()

    def profile_set(self):
        return Profile.objects.filter(classgroup=self)

    def __unicode__(self):
        return self.name
