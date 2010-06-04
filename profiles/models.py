from django.db import models
from django.contrib.auth.models import User
import datetime

class Profile(models.Model):
    """A user profile. Can be useful for students, to define classgroups."""
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(blank=False, max_length=150)
    last_name = models.CharField(blank=False, max_length=150)
    birth_date = models.DateField(default=datetime.datetime.today)
    classgroup = models.ForeignKey('ClassGroup', null=True, blank=True)


class ClassGroup(models.Model):
    name = models.CharField(blank=False, max_length=150)
    campus = models.ForeignKey('locations.Campus', related_name="campus")
    cursus = models.ForeignKey('pedagogy.Cursus', related_name="cursus")

    def __unicode__(self):
        return self.name
