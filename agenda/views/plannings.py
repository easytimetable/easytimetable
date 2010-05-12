# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.utils import simplejson

# app import
from agenda.views import render_to_response
from agenda.models import 

"""List of django views for planning management

"""

def get_planning(request, what=None, extra_context={}, **kwargs=None):
    """Return the planning for `what`. What determines the method we will use
    to fetch the informations through the model manager.

    Special parameters can be set in `extra_parameters`.

    """
    if request.META:
        pass
    pass

def add_event(request):
    pass

def update_event(request)
    pass

def add_course_event(request):
    pass

def update_course_event(request, class_event_id):
    pass

def delete_event(request, event_id):
    pass
