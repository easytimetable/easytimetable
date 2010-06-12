from django.db import models
from django.contrib.auth.models import User
import datetime

from managers import ClassGroupManager

class Profile(models.Model):
    """A user profile. Can be useful for students, to define classgroups."""
    user = models.ForeignKey(User, unique=True)
    date_joined = models.DateField(default=datetime.datetime.today)
    classgroup = models.ForeignKey('ClassGroup', null=True, blank=True)
    is_teacher = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    def list_managed_campuses(self):
        return ", ".join([campus.name for campus in self.campus_managed.all()])
    
    def can_manage_university(self, university_id=None):
        """tell if the user can do university related stuff (CRUD)"""
        return self.user.is_staff
    
    def can_manage_campus(self, campus_id=None):
        """tell if the user can manage campuses"""
        if self.user.is_staff:
            return True
        else:
            return self.campus_managed.filter(id=campus_id) is not None
        
    def can_manage_classgroup(self, classgroup_id=None):
        """tell if the user can manage classgroups"""
        if self.user.is_staff:
            return True
        if classgroup_id is None:
            return self.class_group_managed is not None
        else:
            return self.class_group_managed.filter(id=classgroup_id)

    def can_manage_cursus(self, cursus_id=None):
        """tell if the user can manage pedagogy related items"""
        if self.user.is_staff:
            return True
        if cursus_id is None:
            return self.cursus_managed is not None
        else:
            return self.cursus_managed.filter(id=cursus_id)

    def can_display_calendar(self):
        """user can display calendar"""
        return True

    def is_student(self):
        """a student have a classgroup"""
        return self.classgroup is not None

    @property
    def can_manage_users(self):
        return self.user.is_staff or self.can_manage_classgroup()

    def has_classgroup(self):
        return (self.classgroup is not None)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def delete(self, *args, **kwargs):
        self.campus_managed.clear() 
        super(Profile, self).delete(*args, **kwargs)


class ClassGroup(models.Model):
    name = models.CharField(blank=False, max_length=150)
    campus = models.ForeignKey('locations.Campus', related_name="class_group")
    cursus = models.ForeignKey('pedagogy.Cursus', related_name="class_group")
    manager = models.ForeignKey('Profile', related_name="class_group_managed")
    
    objects = ClassGroupManager()

    def profile_set(self):
        return Profile.objects.filter(classgroup=self)

    def __unicode__(self):
        return "%s - %s" % (self.campus.name, self.name)
