from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ObjectDoesNotExist


from managers import WhenManager
from locations.models import Place, Campus, University
from vobject.icalendar import Component, dateTimeToString

class When(models.Model):
    date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    event = models.ForeignKey('Event')
    objects = WhenManager()
    
    def __unicode__(self):
        return self.date.strftime('%d-%B-%Y')

    def to_vevent(self):
        vevent = Component('vevent')
        vevent.add('dtstart').value = dateTimeToString(self.date)
        vevent.add('dtstamp').value = dateTimeToString(date.fromtimestamp(0))
        vevent.add('dtend').value = dateTimeToString(self.date +\
                datetime.timedelta(hours=self.event.duration))
        vevent.add('summary').value = self.event.name
        try:
            place = "%s : %s" % (self.event.places.get().name,
                                  self.event.places.get().address)
        except ObjectDoesNotExist:
            place = self.event.place_text
        vevent.add('location').value = place
        return vevent
    
    def to_fullcalendar_dict(self, is_editable=lambda when:False,
    css_class='undef'):
        """Return this object under a FullCalendar compatible dict format.

        The is_editable callable is called with the 

        """
        dct = { 'title' : self.event.name,
                'id' : self.id,
                'event_id': self.event_id,
                'allDay' : False,
                'start' : self.date.isoformat(),
                'end' : (self.date +
                datetime.timedelta(hours=self.event.duration)).isoformat(),
                'editable' : is_editable(self),
                'className' : css_class,
            }
        return dct

class Who(models.Model):
    """The Who model has some references to different others models.

    To know who is concerned by an event, it have a method that return this
    informations.
    """
    event = models.ForeignKey('Event')
    user = models.ForeignKey(User, null=True, blank=True)
    classgroup = models.ForeignKey('profiles.ClassGroup', null=True, blank=True)
    cursus = models.ForeignKey('pedagogy.Cursus', null=True, blank=True)
    campus = models.ForeignKey('locations.Campus', null=True, blank=True)
    university = models.ForeignKey('locations.University', null=True, blank=True)
    is_contributor = models.BooleanField(default=False)

    # set to true if it concerns everyone.
    is_universal = models.BooleanField(default=False)

class Event(models.Model):
    name = models.CharField(blank=False, max_length=150)
    duration = models.PositiveIntegerField(blank=False, null=False)
    places = models.ManyToManyField('locations.Place', null=True, blank=True)
    subject_modality = models.ForeignKey('pedagogy.SubjectModality', null=True,
    blank=True)
    force_display = models.BooleanField(default=False)
    place_text = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.name
