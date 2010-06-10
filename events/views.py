"""List of django views for planning management

"""

# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import simplejson as json

# python imports
import functools
from datetime import date, datetime, timedelta

# app imports
from events.models import When, Who, Event
from pedagogy.models import SubjectModality
from utils.shortcuts import render_to_response
from events.forms import UserEventForm, CampusEventForm, ClassgroupEventForm,\
MoveEventForm, ClassgroupSelectorForm, CampusSelectorForm
from events.managers import WhenManager
    
def is_event_editable(user, when):
    events = when.event.who_set.filter(user=user).count()
    if events >= 1:
        return True
    if when.event.subject_modality and when.event.subject_modality.manager.user == user:
        return True
    if when.event.who_set.filter(campus__manager=user).count() > 0:
        return True
    return False
    
@login_required
def get_planning(request, what=None, what_arg=None, extra_context={}, **kwargs):
    """Return the planning for `what`. What determines the method we will use
    to fetch the informations through the model manager.

    Special parameters can be set in `extra_parameters`.
    This mainly return the JSON to be parsed by the calendar client.

    """
    start_date = date.fromtimestamp(int(request.GET["start"]))
    end_date = date.fromtimestamp(int(request.GET["end"]))
    #We don't want people to make too big queries

    if (end_date - start_date).days > 50:
        end_date = start_date

    # partial to not give the request to the model.
    partial_is_editable = functools.partial(is_event_editable, request.user)
    w = When.objects.user_planning(request.user, what, start_date, end_date,\
    what_arg)
    if what == "classgroup":
        what = "%s-%s" % (what, int(what_arg) % 5)
    d = [p.to_fullcalendar_dict(partial_is_editable, what) for p in w]
    return HttpResponse(json.dumps(d))

@login_required
def add_event(request, what=None, what_arg=None, extra_context={}, **kwargs):
    if what == "classgroup":
        return add_classgroup_event(request)
    if what == "campus":
        return add_campus_event(request)
    if what == "my_user":
        return add_user_event(request)
    if what == "my_university":
        pass

@login_required
def add_user_event(request):
    if request.POST:
        form = UserEventForm(data=request.POST, prefix="user")
        if form.is_valid():
            event = Event(name=form.cleaned_data['name'],
                          duration=form.cleaned_data['duration'], 
                          place_text=form.cleaned_data['place_text'])
            event.save()
            who = Who(user=request.user, event=event)
            who.save()
            edate = "%s %s" % (form.cleaned_data['date'],
                form.cleaned_data['start_hour'])
            edate = datetime.strptime(edate, "%Y-%m-%d %H")
            when = When(date=edate, event=event)
            when.save()
            j = when.to_fullcalendar_dict(lambda when:True, "my_user")
            return HttpResponse(json.dumps(j))
        else:
            return False

@login_required
def move_event(request, when_id):
    if request.POST:
        when = When.objects.get(id=when_id)
        if not is_event_editable(request.user, when):
            return False
        form = MoveEventForm(data=request.POST)
        if form.is_valid():
            offset = timedelta(days=form.cleaned_data['days'],
                                minutes=form.cleaned_data['minutes'])
            n_date = when.date + offset
            when.date = n_date
            when.save()
            j = when.to_fullcalendar_dict(lambda when:True, "moved")
            return HttpResponse(json.dumps(j))
        else:
            return False


def add_course_event(request):
    pass

def update_course_event(request, class_event_id):
    pass

def delete_event(request, event_id):
    pass

@login_required
def display_calendar(request):
    user_form = UserEventForm(prefix="user")
    return render_to_response('calendar.html', {
        'user_form': user_form, 
    }, request)

@login_required
def display_campus_mgr_calendar(request):
    campus_form = CampusEventForm(prefix="campus", user=request.user)
    classgroup_form = ClassgroupEventForm(prefix="classgroup", user=request.user)
    campus_selector_form = CampusSelectorForm(user=request.user, prefix="cmp_selector")
    classgroup_selector_form = ClassgroupSelectorForm(user=request.user,
    prefix="cg_selector")
    return render_to_response('campus_manager_calendar.html', {
        'campus_form': campus_form, 
        'classgroup_form': classgroup_form, 
        'classgroup_selector_form': classgroup_selector_form,
        'campus_selector_form': campus_selector_form,
    }, request)


@login_required
def add_classgroup_event(request):
    if request.POST:
        form = ClassgroupEventForm(user=request.user, data=request.POST,
                                   prefix="classgroup")
        when = form.save()
        j = when.to_fullcalendar_dict(lambda when:True, "classgroup")
        return HttpResponse(json.dumps(j))
    else:
        return False

@login_required
def add_campus_event(request):
    if request.POST:
        form = CampusEventForm(user=request.user, data=request.POST,
                                   prefix="campus")
        when = form.save()
        j = when.to_fullcalendar_dict(lambda when:True, "campus")
        return HttpResponse(json.dumps(j))
    else:
        return False

def update_event(request, when_id):
    when = get_object_or_404(When, pk=when_id)
    if when.event.subject_modality:
        form = None
    elif when.event.who_set.filter(user=request.user).count() > 0:
        data = {'name' : when.event.name,
                'date' : when.date.strftime("%Y-%m-%d"),
                'start_hour' : when.date.strftime("%H"),
                'duration' : when.event.duration,
                'place_text' : when.event.place_text,
               }
        if request.POST:
            form = UserEventForm(data=request.POST)
            if form.is_valid():
                f = form.cleaned_data
                when.event.name = f['name']
                when.event.duration = f['duration']
                when.event.place_text = f['place_text']
                edate = "%s %s" % (form.cleaned_data['date'],
                    form.cleaned_data['start_hour'])
                edate = datetime.strptime(edate, "%Y-%m-%d %H")
                when.date = edate
                when.event.save()
                when.save()
                j = when.to_fullcalendar_dict(lambda when:True, "moved")
                return HttpResponse(json.dumps(j))
            return render_to_response('edit_user_calendar.html', {
                'form': form,}, request)
        form = UserEventForm(data=data)
        return render_to_response('edit_user_calendar.html', {
            'form': form,}, request)
