import datetime
from django.db import models

class ClassGroupManager(models.Manager):
    def get_managed_by(self, user=None):
        return super(ClassGroupManager, self).get_query_set().all()

