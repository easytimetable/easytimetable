"""List of django views for planning management

"""

# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import simplejson as json
from django.core.exceptions import ObjectDoesNotExist

# python imports
import functools
from datetime import date, datetime, timedelta
from vobject import iCalendar

# app imports
from events.models import When, Who, Event
from pedagogy.models import SubjectModality
from utils.shortcuts import render_to_response
from events.forms import UserEventForm, CampusEventForm, ClassgroupEventForm,\
MoveEventForm, ClassgroupSelectorForm, CampusSelectorForm, MySelectorForm
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

def get_ical(request, what=None, what_arg=None, must=True, extra_context={}, **kwargs):
    start_date = date.min
    end_date = date.max
    w = When.objects.user_planning(request.user, what, start_date, end_date,\
    what_arg)
    cal = iCalendar()
    cal.add('method').value = 'PUBLISH'  # IE/Outlook needs this
    for e in w:
        cal.add(e.to_vevent())
    icalstream = cal.serialize()
    response = HttpResponse(icalstream, mimetype='text/calendar')
    if what_arg is None:
        what_arg = ""
    response['Filename'] = '%s%s.ics' % (what, what_arg)  # IE needs this
    response['Content-Disposition'] = 'attachment; filename=%s' %\
        response['Filename']
    return response


@login_required
def list_events(request):
    to_fetch = ("mandatory", "my_user", "my_classgroup", "my_campus",
    "my_university")
    events = set()
    start_date = datetime.now()
    end_date = datetime.now()+timedelta(days=7)
    for source in to_fetch:
        fetched = When.objects.user_planning(request.user, source,
                                         start_date, end_date)
        for event in list(fetched):
            event.resource = source
        events = events | set(fetched)
    return render_to_response('list_events.html', {'whens' : events,} , request)

        

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
            when = form.save()
            who = Who(user=request.user, event=when.event)
            who.save()
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

@login_required
def resize_event(request, when_id):
    if request.POST:
        when = When.objects.get(id=when_id)
        if not is_event_editable(request.user, when):
            return False
        form = MoveEventForm(data=request.POST)
        if form.is_valid():
            duration = int(form.cleaned_data['days']) * 24 +\
                       int(form.cleaned_data['minutes']) / 60
            when.event.duration = when.event.duration + duration
            when.event.save()
            return HttpResponse("ok")
        else:
            return HttpResponse("!ok")

@login_required
def delete_event(request, when_id):
    if request.POST:
        when = When.objects.get(id=when_id)
        if not is_event_editable(request.user, when):
            return HttpResponse("!ok", status=403)
        when.event.delete()
        return HttpResponse("ok")
    return HttpResponse("!ok", status=500)

@login_required
def display_calendar(request):
    #Standard forms
    user_form = UserEventForm(prefix="user")
    my_selector_form = MySelectorForm(prefix="my_selector")
    forms = { 'user_form': user_form,}
    selectors = {'my_selector_form': my_selector_form,}

    if request.user.get_profile().can_manage_campus():
        forms['campus_form'] = CampusEventForm(prefix="campus",
            user=request.user)
        forms['classgroup_form'] = ClassgroupEventForm(prefix="classgroup",
            user=request.user)
        selectors['campus'] = CampusSelectorForm(
            prefix="cmp_selector", user=request.user)
        selectors['classgroup'] = ClassgroupSelectorForm(
            prefix="cg_selector", user=request.user)
        selectors['my_selector_form'] = MySelectorForm(prefix="my_selector",
            what=["my_user"])

    forms.update(selectors)
    return render_to_response('calendar.html', {'forms' : forms,} , request)

    

@login_required
def display_campus_mgr_calendar(request):
    user_form = UserEventForm(prefix="user")
    my_selector_form = MySelectorForm(prefix="my_selector", what=["my_user"])
    return render_to_response('calendar.html', {
        'campus_form': campus_form, 
        'user_form': user_form, 
        'classgroup_form': classgroup_form, 
        'classgroup_selector_form': classgroup_selector_form,
        'campus_selector_form': campus_selector_form,
        'my_selector_form': my_selector_form,
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
    form = None
    when = get_object_or_404(When, pk=when_id)
    data = {'name' : when.event.name,
            'date' : when.date.strftime("%Y-%m-%d"),
            'start_hour' : int(when.date.strftime("%H")),
            'duration' : int(when.event.duration),
            'place_text' : when.event.place_text,
           }
    if when.event.subject_modality:
        data.update({'place' : when.event.places.get().id,
                     'classgroup' :
                     when.event.who_set.get(classgroup__isnull=False).classgroup_id,
                     'modality' : 
                     when.event.subject_modality.type,
                     'subject' : 
                     when.event.subject_modality.subject.id, })
        if request.POST:
            form = ClassgroupEventForm(user=request.user, data=request.POST)
        else:
            form = ClassgroupEventForm(user=request.user, initial=data)
    elif when.event.who_set.filter(user=request.user).count() > 0:
        if request.POST:
            form = UserEventForm(data=request.POST)
        else:
            form = UserEventForm(initial=data)
    elif when.event.who_set.filter(campus__manager=request.user).count() > 0:
        try:
            place = when.event.places.get().id
        except ObjectDoesNotExist:
            place_id = None
        data.update({'place' : place_id,
                     'campus' : 
                     when.event.who_set.get(campus__isnull=False).campus.id,
                     })
        if request.POST:
            form = CampusEventForm(data=request.POST, user=request.user)
        else:
            form = CampusEventForm(initial=data, user=request.user)
    if request.POST:
        if form.is_valid():
            when = form.save(when)
            j = when.to_fullcalendar_dict(lambda when:True, "moved")
            return HttpResponse(json.dumps(j))
    return render_to_response('edit_user_calendar.html', {
            'form': form,}, request)
