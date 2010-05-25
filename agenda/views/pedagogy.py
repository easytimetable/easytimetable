# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
 
# app import
from agenda.views import render_to_response
from agenda.models import Cursus, StudyPeriod, Subject, SubjectModality, ClassGroup
from agenda.forms import CursusForm, StudyPeriodForm, SubjectForm, SubjectModalityForm, ClassGroupForm

# -- Study Period related views ----------------------------------------------

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
    return render_to_response("agenda/pedagogy/get_studyperiod.html", {
        'studyperiod': studyperiod,
    }, request)
    
@login_required
def list_studyperiods(request):
    studyperiods = StudyPeriod.objects.all()
    return render_to_response("agenda/pedagogy/list_studyperiods.html", {
        'studyperiods': studyperiods,
    }, request)

    
# -- Subject related views ----------------------------------------------------

@login_required
def add_subject(request):
    if request.POST:
        form = SubjectForm(data=request.POST)
        if form.is_valid():
            from ipdb import set_trace
            set_trace()
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
    }, request)

@login_required
def list_subjects(request):
    subjects = Subject.objects.all()
    return render_to_response("agenda/pedagogy/list_subjects.html", {
        'subjects': subjects,
    }, request)

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
    subjectmodalities = SubjectModality.objects.all()
    return render_to_response("agenda/pedagogy/list_subjectmodalities.html", {
        'subjectmodalities': subjectmodalities,
    }, request)

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
    cursuses = Cursus.objects.all()
    return render_to_response("agenda/pedagogy/list_cursuses.html", {
        'cursuses': cursuses,
    }, request)

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
    classgroups = ClassGroup.objects.all()
    return render_to_response("agenda/pedagogy/list_classgroups.html", {
        'classgroups': classgroups,
    }, request)

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
