# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _

# app import
from utils.shortcuts import render_to_response
from pedagogy.models import StudyPeriod, Subject, SubjectModality

def get_studyperiod(request, studyperiod_id):
    studyperiod = get_object_or_404(StudyPeriod, pk=studyperiod_id)
    # get the list of subjects for this study period, with a list of 
    # subject modalities
    subject_modalities = {}
    for s in Subject.objects.filter(study_period=studyperiod): 
        subject_modalities[s.name] = dict([(sm.type, sm.planned_hours) for sm in s.modalities.all()])

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

    return render_to_response("get_studyperiod.html", {
        'studyperiod': studyperiod,
        'series': final_output,
        'subjects' : subject_modalities.keys(),
    }, request)
