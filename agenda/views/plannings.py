# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from agenda.models import When
from django.utils import simplejson as json
from agenda.managers import EventManager

# app import
from agenda.views import render_to_response

"""List of django views for planning management

"""

def get_planning(request, what=None, extra_context={}, **kwargs):
    """Return the planning for `what`. What determines the method we will use
    to fetch the informations through the model manager.

    Special parameters can be set in `extra_parameters`.

    """
    if what == "test":
        w = When.objects.all()
        d = [p.to_fullcalendar_dict() for p in w]
        return HttpResponse(json.dumps(d))

def add_event(request):
    pass

def update_event(request):
    pass

def add_course_event(request):
    pass

def update_course_event(request, class_event_id):
    pass

def delete_event(request, event_id):
    pass

def display_calendar(request):
    return render_to_response('agenda/plannings/calendar.html', {}, request)
