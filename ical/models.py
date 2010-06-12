from django.db import models
from django.contrib.auth.models import User


class IcalLink(models.Model):
    """Ical access list"""
    calendar_type = models.CharField(max_length=12, blank=False)
    calendar_id = models.IntegerField(blank=True, null=True)
    hash = models.CharField(max_length=140, blank=False)
    user = models.ForeignKey(User, related_name='ical_link')
