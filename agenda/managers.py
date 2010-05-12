import datetime

from django.db import models

class EventManager(models.Manager):
    def for_user(self, user):
        return self.get_query_set().filter

