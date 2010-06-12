from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404, redirect
from ical.models import IcalLink
from profiles.models import ClassGroup
from locations.models import Campus
from uuid import uuid1
from utils.shortcuts import render_to_response
from events.views import get_ical


@login_required
def get_ical_link_hash(request, what=None, what_arg=None):
    obj, created = IcalLink.objects.get_or_create(calendar_type=what,
                                                  calendar_id=what_arg,
                                                  user=request.user,
                      defaults={'hash': "%s" % uuid1() })
    return obj;

def get_feed(request, hash):
    link = get_object_or_404(IcalLink, hash=hash)
    request.user = link.user
    return get_ical(request, link.calendar_type, link.calendar_id,
    mandatory=True)


@login_required
def display_ical_mgmnt(request):
    ical_feeds = []
    nical_feeds = []
    ical_feeds.append(("my_user", None, "My calendar"))
    if request.user.get_profile().can_manage_campus():
        for campus in Campus.objects.get_managed_by(request.user):
            ical_feeds.append(("campus", campus.id, campus.name)) 
        for classgroup in ClassGroup.objects.get_managed_by(request.user):
            ical_feeds.append(("classgroup", classgroup.id, classgroup.name))
    else:
        ical_feeds.append(("my_classgroup", None, "My class"))
        ical_feeds.append(("my_campus", None, "My campus"))
    for type, id, name in ical_feeds:
        hash = get_ical_link_hash(request, type, id).hash
        if id is None:
            id = ''
        nical_feeds.append((type, id, name, hash))
    return render_to_response('display_ical_mgmnt.html', 
                             { 'feeds': nical_feeds,}, request)

@login_required
def reset_hash(request, hash):
    IcalLink.objects.get(user=request.user,
                         hash=hash).delete()
    return redirect("ical:display_ical_mgmnt")
        
