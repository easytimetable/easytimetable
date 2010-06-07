import datetime
from django.db import models

class CampusManager(models.Manager):
    def get_managed_by(self, user=None):
        return super(CampusManager, self).get_query_set().filter(manager=user)

class PlaceManager(models.Manager):
    def get_managed_by(self, user=None):
        return super(PlaceManager, self).get_query_set().filter(
                                                         campus__manager=user)

