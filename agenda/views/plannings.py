"""List of django views for planning management

"""

# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from agenda.models import When
from django.utils import simplejson as json

# python imports
import functools

# app imports
from agenda.views import render_to_response
from agenda.forms.plannings import UserEventForm 

def get_planning(request, what=None, extra_context={}, **kwargs):
    """Return the planning for `what`. What determines the method we will use
    to fetch the informations through the model manager.

    Special parameters can be set in `extra_parameters`.

    """
    def define_is_editable(request, when):
        return (when.id % 2 == 0)
    
    # partial to not give the request to the model.
    partial_is_editable = functools.partial(define_is_editable, request)
    if what == "test":
        w = When.objects.all()
        d = [p.to_fullcalendar_dict(partial_is_editable) for p in w]
        return HttpResponse(json.dumps(d))

def add_user_event(request):
    if request.POST:
        form = UserEventForm(data=request.POST)
    else:
        form = UserEventForm()

    return render_to_response('agenda/plannings/add_user_event.html', {
        'form': form,
    }, request)

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
