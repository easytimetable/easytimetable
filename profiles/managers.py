import datetime
from django.db import models

class ClassGroupManager(models.Manager):
    def get_managed_by(self, user=None):
        from ipdb import set_trace; set_trace()
        if user.is_staff:
            return super(ClassGroupManager, self).get_query_set().all()
        return super(ClassGroupManager,
        self).get_query_set().filter(campus__manager=user)

    def get_inhabited_by(self, user=None):
        return super(ClassGroupManager, self).get_query_set().filter(profile=user.get_profile())
