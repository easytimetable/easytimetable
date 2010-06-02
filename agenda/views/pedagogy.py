# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.utils import simplejson as json

# app import
from agenda.views import render_to_response, crud
from agenda.models import Cursus, StudyPeriod, Subject, SubjectModality, ClassGroup
from agenda.forms import CursusForm, StudyPeriodForm, SubjectForm, SubjectModalityForm, ClassGroupForm

# -- Study Period related views ----------------------------------------------

@login_required
def add_studyperiod(request, cursus_id = None):
    if request.POST:
        form = StudyPeriodForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:list_studyperiods')
    else:
        form = StudyPeriodForm(initial={"cursus":Cursus.objects.get(id=cursus_id)})
    return render_to_response('agenda/pedagogy/add_studyperiod.html', {
        'form' : form,
    }, request)
    
@login_required
def delete_studyperiod(request, studyperiod_id):
    studyperiod = get_object_or_404(StudyPeriod, pk=studyperiod_id)
    studyperiod.delete()
    request.user.message_set.create(message=_("%s studyperiod has been deleted.") % studyperiod.name)
    return redirect('agenda:list_studyperiods')
    
@login_required
def update_studyperiod(request, studyperiod_id):
    studyperiod = get_object_or_404(StudyPeriod, pk=studyperiod_id)
    if request.POST:
        form = StudyPeriodForm(data=request.POST, instance=studyperiod)
        form.save()
        return redirect('agenda:list_studyperiods')
    form = StudyPeriodForm(instance=studyperiod)
    return render_to_response("agenda/pedagogy/add_studyperiod.html", {
        'form': form,
    }, request)
    
@login_required
def get_studyperiod(request, studyperiod_id):
    studyperiod = get_object_or_404(StudyPeriod, pk=studyperiod_id)
    # get the list of subjects for this study period, with a list of 
    # subject modalities
    subject_modalities = {}
    for s in Subject.objects.filter(study_period=studyperiod): 
        subject_modalities[s.name] = dict([(sm.type, sm.planned_hours) for sm in s.subjectmodality_set.all()])

    output = dict([(type,{
            'name':dict(SubjectModality.TYPE_CHOICES)[type], 
            'data': [],
        }) for type, null in SubjectModality.TYPE_CHOICES])
    for (subject, modalities) in subject_modalities.items():
        for key,value in modalities.items():
            output[key]['data'].append(int(value))

    final_output = []
    for key, value in output.items():
        final_output.append(value)
        
    return render_to_response("agenda/pedagogy/get_studyperiod.html", {
        'studyperiod': studyperiod,
        'series': final_output,
        'subjects' : subject_modalities.keys(),
    }, request)
    
@login_required
def list_studyperiods(request):
    fields = [('Study Period', 'name'), ('Cursus', 'cursus.name')]
    return crud.list(StudyPeriod, fields, request, extra_context={
        'form': StudyPeriodForm(),
    })

    
# -- Subject related views ----------------------------------------------------

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
    request.user.message_set.create(message=_("%s subject has been deleted.") % subject.name)
    return redirect('agenda:list_subjects')

@login_required
def update_subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.POST:
        form = SubjectForm(data=request.POST, instance=subject)
        form.save()
        return redirect('agenda:list_subjects')
    form = SubjectForm(instance=subject)
    return render_to_response("agenda/pedagogy/add_subject.html", {
        'form': form,
    }, request)

@login_required    
def get_subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render_to_response("agenda/pedagogy/get_subject.html", {
        'subject': subject,
        'modalities': subject.subjectmodality_set.all(),
    }, request)

@login_required
def list_subjects(request):
    fields = [('Subject', 'name'), ('Cursus', 'study_period.cursus.name'), ('Study Period', 'study_period.name')]
    return crud.list(Subject, fields, request, extra_context={
        'form': SubjectForm(),
    })

# -- Subject modality ---------------------------------------------------------

@login_required
def add_subjectmodality(request):
    if request.POST:
        form = SubjectModalityForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:list_subjectmodalities')
    else:
        form = SubjectModalityForm()
    return render_to_response('agenda/pedagogy/add_subjectmodality.html', {
        'form' : form,
    }, request)

@login_required
def delete_subjectmodality(request, subjectmodality_id):
    subjectmodality = get_object_or_404(SubjectModality, pk=subjectmodality_id)
    subjectmodality.delete()
    request.user.message_set.create(message=_("%s subjectmodality has been deleted.") % subjectmodality.name)
    return redirect('agenda:list_subjectmodalities')

@login_required
def update_subjectmodality(request, subjectmodality_id):
    subjectmodality = get_object_or_404(SubjectModality, pk=subjectmodality_id)
    if request.POST:
        form = SubjectModalityForm(data=request.POST, instance=subjectmodality)
        form.save()
        return redirect('agenda:list_subjectmodalities')
    form = SubjectModalityForm(instance=subjectmodality)
    return render_to_response("agenda/pedagogy/add_subjectmodality.html", {
        'form': form,
    }, request)

@login_required
def get_subjectmodality(request, subjectmodality_id):
    subjectmodality = get_object_or_404(SubjectModality, pk=subjectmodality_id)
    return render_to_response("agenda/pedagogy/get_subjectmodality.html", {
        'subjectmodality': subjectmodality,
    }, request)

@login_required
def list_subjectmodalities(request):
    fields = [('Subject Modality', 'type'), ('Subject', 'subject.name')]
    return crud.list(SubjectModality, fields, request, extra_context={
        'form': SubjectModalityForm(),
    })

# -- Cursus -------------------------------------------------------------------

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
    request.user.message_set.create(message=_("%s cursus has been deleted.") % cursus.name)
    return redirect('agenda:list_cursuses')

@login_required
def get_cursus(request, cursus_id):
    cursus = get_object_or_404(Cursus, pk=cursus_id)
    return render_to_response("agenda/pedagogy/get_cursus.html", {
        'cursus': cursus,
    }, request)

@login_required
def list_cursuses(request):
    fields = [('Cursus','name'), ('Classes', 'classgroup_set.count')]
    return crud.list(Cursus, fields, request, extra_context={
        'form': CursusForm(),
    })


@login_required
def update_cursus(request, cursus_id):
    cursus = get_object_or_404(Cursus, pk=cursus_id)
    if request.POST:
        form = CursusForm(data=request.POST, instance=cursus)
        form.save()
        return redirect('agenda:list_cursuses')
    form = CursusForm(instance=cursus)
    return render_to_response("agenda/pedagogy/add_cursus.html", {
        'form': form,
    }, request)


# -- Class --------------------------------------------------------------------

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
