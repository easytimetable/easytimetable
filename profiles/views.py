# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# app import
from utils.shortcuts import render_to_response
from utils import crud
from profiles.models import ClassGroup, Profile
from pedagogy.models import Subject
from profiles.forms import ClassGroupForm, StudentForm, CampusManagerForm

@login_required
def add_classgroup(request, campus_id=None):
    if request.POST:
        form = ClassGroupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiles:list_classgroups')
    else:
        form = ClassGroupForm({'campus':campus_id})
    return render_to_response("add_classgroup.html", {
        'form': form,
    }, request)

@login_required
def list_classgroup_subjects(request,classgroup_id):
    fields = [('id','id'), ('name', 'name')]
    return crud.list(request, fields,
        queryset = Subject.objects.filter(
             study_period__cursus__class_group__id=classgroup_id))

def delete_campus_manager(request, user_id):
    profile = Profile.objects.get(user__id=user_id) 
    profile.campus_managed.clear()
    return redirect('profiles:list_campus_managers')
