import datetime
from django.db import models

class CampusManager(models.Manager):
    def get_managed_by(self, user=None):
        if user.is_staff:
            return super(CampusManager, self).get_query_set().all()
        return super(CampusManager, self).get_query_set().filter(manager=user)
    
    def get_inhabited_by(self, user=None):
        classgroup = user.get_profile().classgroup
        if classgroup:
            return super(CampusManager,
            self).get_query_set().filter(class_group=classgroup)
        return super(CampusManager,self).get_query_set().none()

class PlaceManager(models.Manager):
    def get_managed_by(self, user=None):
        if user.is_staff:
            return super(PlaceManager, self).get_query_set().all()
        return super(PlaceManager, self).get_query_set().filter(campus__manager=user)

