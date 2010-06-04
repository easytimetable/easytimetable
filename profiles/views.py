# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

# app import
from utils.shortcuts import render_to_response
from utils import crud
from profiles.models import ClassGroup
from profiles.forms import ClassGroupForm

@login_required
def add_classgroup(request):
    if request.POST:
        form = ClassGroupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:list_classgroups')
    else:
        form = ClassGroupForm()
    return render_to_response("agenda/pedagogy/add_classgroup.html", {
        'form': form,
    }, request)

@login_required
def delete_classgroup(request, classgroup_id):
    classgroup = get_object_or_404(ClassGroup, pk=classgroup_id)
    classgroup.delete()
    request.user.message_set.create(message=_("%s classgroup has been deleted.") % classgroup.name)
    return redirect('agenda:list_classgroups')

@login_required
def list_classgroups(request):
    fields = [('Classe','name'), ('Students', 'profile_set.count')]
    return crud.list(ClassGroup, fields, request, extra_context={
        'form': ClassGroupForm(),
    })

@login_required
def get_classgroup(request, classgroup_id):
    classgroup = get_object_or_404(ClassGroup, pk=classgroup_id)
    return render_to_response("agenda/pedagogy/get_classgroup.html", {
        'classgroup' : classgroup,
    }, request)

@login_required
def update_classgroup(request, classgroup_id):
    classgroup = get_object_or_404(ClassGroup, pk=classgroup_id)
    if request.POST:
        form = ClassGroupForm(data=request.POST, instance=classgroup)
        form.save()
        return redirect('agenda:list_classgroups')
    form = ClassGroupForm(instance=classgroup)
    return render_to_response("agenda/pedagogy/add_classgroup.html", {
        'form': form,
    }, request)
