# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

# app import
from agenda.views import render_to_response
from agenda.models import ClassGroup
from agenda.forms import ClassGroupForm

def get_classgroup(request, classgroup_id):
    classgroup = get_object_or_404(ClassGroup, pk=classgroup_id)
    return render_to_response('agenda/classgroups/get.html',
                              { 'classgroup' : classgroup },
                              request)

@login_required
def delete_classgroup(request, classgroup_id):
    classgroup = get_object_or_404(ClassGroup, pk=classgroup_id)
    classgroup.delete()
    request.user.message_set.create(message=_("%s classgroup has been deleted.") % classgroup.name)
    return redirect('agenda:list_classgroups')


def update_classgroup(request, classgroup_id):
    pass

@login_required
def add_classgroup(request):
    if request.POST:
        form = ClassGroupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:list_classgroups')
    else:
        form = ClassGroupForm()
    return render_to_response("agenda/classgroups/add_classgroup.html", {
                                  'form': form, }
                                  , request)

def list_classgroups(request):
    classgroups = ClassGroup.objects.all()
    return render_to_response("agenda/classgroups/list_classgroups.html", {
        'classgroups': classgroups,
    }, request)

