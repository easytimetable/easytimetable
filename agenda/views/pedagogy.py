# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
 
# app import
from agenda.views import render_to_response
from agenda.models import Cursus
from agenda.forms import CursusForm

"""Study Period
"""

def add_studyperiod(request):
	"""
	"""

def delete_studyperiod(request, studyperiod_id):
	"""
	"""

def update_studyperiod(request, studyperiod_id):
	"""
	"""
	
def get_studyperiod(request):
	"""
	"""

def list_studyperiods(request):
	"""
	"""

"""Subject

"""

def add_subject(request):
	"""
	"""

def delete_subject(request, subject_id):
	"""
	"""

def update_subject(request, subject_id):
	"""
	"""
	
def get_subject(request):
	"""
	"""

def list_subjects(request):
	"""
	"""

"""Subject modality

"""
def add_subject_modality(request):
	"""
	"""

def delete_subject_modality(request, subject_modality_id):
	"""
	"""

def update_subject_modality(request, subject_modality_id):
	"""
	"""
	
def get_subject_modality(request):
	"""
	"""

def list_subject_modalities(request):
	"""
	"""

"""Cursus
"""
@login_required
def add_cursus(request):
    if request.POST:
        form = CursusForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:list_cursuses')
    else:
        form = CursusForm()
    return render_to_response('agenda/pedagogy/add_cursus.html', {
        'form' : form,
    }, request) 

@login_required
def delete_cursus(request, cursus_id):
    cursus = get_object_or_404(Cursus, pk=cursus_id)
    cursus.delete()
    return redirect('agenda:list_cursuses')

@login_required
def get_cursus(request, cursus_id):
    cursus = get_object_or_404(Cursus, pk=cursus_id)
    return render_to_response("agenda/pdagogy/get_cursus.html", {
        'cursus': cursus,
    }, request)

@login_required
def list_cursuses(request):
    cursuses = Cursus.objects.all()
    return render_to_response("agenda/pedagogy/list_cursuses.html", {
        'cursuses': cursuses,
    }, request)

@login_required
def update_cursus(request, cursus_id):
#    cursus = get_object_or_404(Cursus, pk=cursus_id)
#    cursus.update()
    pass

