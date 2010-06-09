from django.conf.urls.defaults import *
from pedagogy.models import Cursus, StudyPeriod, Subject, SubjectModality 
from pedagogy.forms import CursusForm, StudyPeriodForm, SubjectForm 

# Generic views

urlpatterns = patterns('utils.crud',

    # -- Studyperiods ----------------------------------------
    (r'^studyperiods/add/$', 'create', {
        'model': StudyPeriod, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_studyperiods', 
    }, 'add_studyperiod'),

    (r'^studyperiods/(?P<object_id>\d+)/update/$', 'update', {
        'model': StudyPeriod, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_studyperiods', 
    }, 'update_studyperiod'),

    (r'^studyperiods/$', 'list', {
        'model': StudyPeriod, 
        'form_class': StudyPeriodForm, 
        'fields': [
            ('Study Period', 'name'), 
            ('Cursus', 'cursus.name')
        ],
    }, 'list_studyperiods'),

    (r'^studyperiods/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': StudyPeriod,
        'post_delete_redirect': 'pedagogy:list_studyperiods'
    }, 'delete_studyperiod'),

    # -- Subjets ----------------------------------------
    (r'^subjects/add/$', 'create', {
        'model': Subject, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_subjects', 
    }, 'add_subject'),

    (r'^subjects/(?P<object_id>\d+)/update/$', 'update', {
        'model': Subject, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_subjects', 
    }, 'update_subject'),

    (r'^subjects/$', 'list', {
        'model': Subject, 
        'form_class': SubjectForm, 
        'fields': [ 
            ('Subject', 'name'), 
            ('Cursus', 'study_period.cursus.name'), 
            ('Study Period', 'study_period.name')
        ],
        }, 'list_subjects'),

    (r'^subjects/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': Subject,
        'post_delete_redirect': 'pedagogy:list_subjects'
    }, 'delete_subject'),
    
    (r'^subjects/(?P<object_id>\d+)/$', 'get', {
        'queryset': Subject.objects.all(), 
        'template_name': 'get_subject.html',
        'template_object_name': 'subject',
    }, 'get_subject'),

    # -- Subjet Modalities ----------------------------------------

    (r'^subject_modalities/add/$', 'create', {
        'model': Subject, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_subject_modalities', 
    }, 'add_subjectmodality'),

    (r'^subject_modalities/(?P<object_id>\d+)/update/$', 'update', {
        'model': Subject, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_subject_modalities', 
    }, 'update_subjectmodality'),

    (r'^subject_modalities/$', 'list', {
        'model': Subject, 
        'form_class': SubjectForm, 
        'fields': [
            ('Subject Modality', 'type'), 
            ('Subject', 'subject.name')
        ], 
        'template': 'list_subject_modalities.html'
    }, 'list_subject_modalities'),

    (r'^subject_modalities/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': Subject,
        'post_delete_redirect': 'pedagogy:list_subject_modalities'
    }, 'delete_subjectmodality'),
    
    (r'^subject_modalities/(?P<object_id>\d+)/$', 'get', {
        'queryset': Subject.objects.all(), 
        'template_name': 'get_subjectmodality.html',
        'template_object_name': 'subjectmodality',
    }, 'get_subjectmodality'),

    # -- Cursuses ----------------------------------------

    (r'^cursuses/add/$', 'create', {
        'model': Cursus, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_cursuses', 
    }, 'add_cursus'),

    (r'^cursuses/(?P<object_id>\d+)/update/$', 'update', {
        'model': Cursus, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_cursuses', 
    }, 'update_cursus'),

    (r'^cursuses/$', 'list', {
        'model': Cursus, 
        'form_class': CursusForm, 
        'fields': [
            ('Cursus','name'), 
            ('Classes', 'classgroup_set.count')
        ],
    }, 'list_cursuses'),

    (r'^cursuses/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': Cursus,
        'post_delete_redirect': 'pedagogy:list_cursuses'
    }, 'delete_cursus'),
    
    (r'^cursuses/(?P<object_id>\d+)/$', 'get', {
        'queryset': Cursus.objects.all(), 
        'template_name': 'get_cursus.html',
        'template_object_name': 'cursus',
    }, 'get_cursus'),
)

# Specific views
urlpatterns += patterns('pedagogy.views',
    (r'^studyperiods/(?P<studyperiod_id>\d+)$', 'get_studyperiod', {}, 'get_studyperiod'),
)
