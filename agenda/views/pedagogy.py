# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
 
# app import
from agenda.views import render_to_response
from agenda.models import Cursus, StudyPeriod, Subject
from agenda.forms import CursusForm, StudyPeriodForm, SubjectForm

"""Study Period
"""
@login_required
def add_studyperiod(request):
	if request.POST:
		form = StudyPeriodForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('agenda:list_studyperiods')
	else:
		form = StudyPeriodForm()
	return render_to_response('agenda/pedagogy/add_studyperiod.html', {
		'form' : form,
	}, request)
	
@login_required
def delete_studyperiod(request, studyperiod_id):
	studyperiod = get_object_or_404(StudyPeriod, pk=studyperiod_id)
	studyperiod.delete()
	return redirect('agenda:list_studyperiods')
	
@login_required
def update_studyperiod(request, studyperiod_id):
	"""
	"""
	
@login_required
def get_studyperiod(request, studyperiod_id):
	studyperiod = get_object_or_404(StudyPeriod, pk=studyperiod_id)
	return render_to_response("agenda/pedagogy/get_studyperiod.html", {
		'studyperiod': studyperiod,
	}, request)
	
@login_required
def list_studyperiods(request):
	studyperiods = StudyPeriod.objects.all()
	return render_to_response("agenda/pedagogy/list_studyperiods.html", {
		'studyperiods': studyperiods,
	}, request)

	
"""Subject

"""
@login_required
def add_subject(request):
	if request.POST:
		form = SubjectForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('agenda:list_subjects')
	else:
		form = SubjectForm()
	return render_to_response('agenda/pedagogy/add_subject.html', {
		'form' : form,
	}, request)

@login_required
def delete_subject(request, subject_id):
	subject = get_object_or_404(Subject, pk=subject_id)
	subject.delete()
	return redirect('agenda:list_subjects')

@login_required
def update_subject(request, subject_id):
	"""
	"""

@login_required	
def get_subject(request, subject_id):
	subject = get_object_or_404(Subject, pk=subject_id)
	return render_to_response("agenda/pedagogy/get_subject.html", {
		'subject': subject,
	}, request)

@login_required
def list_subjects(request):
	subjects = Subject.objects.all()
	return render_to_response("agenda/pedagogy/list_subjects.html", {
		'subjects': subjects,
	}, request)

"""Subject modality

"""

@login_required
def add_subject_modality(request):
	"""
	"""

@login_required
def delete_subject_modality(request, subject_modality_id):
	"""
	"""

@login_required
def update_subject_modality(request, subject_modality_id):
	"""
	"""

@login_required
def get_subject_modality(request):
	"""
	"""

@login_required
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
    return render_to_response("agenda/pedagogy/get_cursus.html", {
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

