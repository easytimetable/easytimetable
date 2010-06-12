from django.conf.urls.defaults import *
from pedagogy.models import Cursus, StudyPeriod, Subject, SubjectModality 
from pedagogy.forms import CursusForm, StudyPeriodForm, SubjectForm 
from acls import crud_acl_handler

# Generic views

urlpatterns = patterns('utils.crud',

    # -- Studyperiods ----------------------------------------
    (r'^studyperiods/add/$', 'create', {
        'model': StudyPeriod, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_studyperiods', 
        'acl_handler': crud_acl_handler("cursus"),
    }, 'add_studyperiod'),

    (r'^studyperiods/(?P<object_id>\d+)/update/$', 'update', {
        'model': StudyPeriod, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_studyperiods', 
        'acl_handler': crud_acl_handler("cursus"),
    }, 'update_studyperiod'),

    (r'^studyperiods/$', 'list', {
        'model': StudyPeriod, 
        'form_class': StudyPeriodForm, 
        'fields': [
            ('Study Period', 'name'), 
            ('Cursus', 'cursus.name')
        ],
        'acl_handler': crud_acl_handler("cursus"),
    }, 'list_studyperiods'),

    (r'^studyperiods/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': StudyPeriod,
        'post_delete_redirect': 'pedagogy:list_studyperiods'
    }, 'delete_studyperiod'),

    # -- Subjets ----------------------------------------
    (r'^subjects/add/$', 'create', {
        'model': Subject,
        'form_class': SubjectForm,
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_subjects', 
        'acl_handler': crud_acl_handler("cursus"),
    }, 'add_subject'),

    (r'^subjects/(?P<object_id>\d+)/update/$', 'update', {
        'model': Subject, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_subjects', 
        'acl_handler': crud_acl_handler("cursus"),
    }, 'update_subject'),

    (r'^subjects/$', 'list', {
        'model': Subject, 
        'form_class': SubjectForm, 
        'fields': [ 
            ('Subject', 'name'), 
            ('Cursus', 'study_period.cursus.name'), 
            ('Study Period', 'study_period.name')
        ],
        'acl_handler': crud_acl_handler("cursus"),
        }, 'list_subjects'),

    (r'^subjects/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': Subject,
        'post_delete_redirect': 'pedagogy:list_subjects',
        'acl_handler': crud_acl_handler("cursus"),
    }, 'delete_subject'),
    
    (r'^subjects/(?P<object_id>\d+)/$', 'get', {
        'queryset': Subject.objects.all(), 
        'template_name': 'get_subject.html',
        'template_object_name': 'subject',
        'acl_handler': crud_acl_handler("cursus"),
    }, 'get_subject'),

    # -- Subjet Modalities ----------------------------------------

    (r'^subject_modalities/add/$', 'create', {
        'model': Subject, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_subject_modalities', 
        'acl_handler': crud_acl_handler("cursus"),
    }, 'add_subjectmodality'),

    (r'^subject_modalities/(?P<object_id>\d+)/update/$', 'update', {
        'model': Subject, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_subject_modalities', 
        'acl_handler': crud_acl_handler("cursus"),
    }, 'update_subjectmodality'),

    (r'^subject_modalities/$', 'list', {
        'model': Subject, 
        'form_class': SubjectForm, 
        'fields': [
            ('Subject Modality', 'type'), 
            ('Subject', 'subject.name')
        ], 
        'template': 'list_subject_modalities.html',
        'acl_handler': crud_acl_handler("cursus"),
    }, 'list_subject_modalities'),

    (r'^subject_modalities/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': Subject,
        'post_delete_redirect': 'pedagogy:list_subject_modalities',
        'acl_handler': crud_acl_handler("cursus"),
    }, 'delete_subjectmodality'),
    
    (r'^subject_modalities/(?P<object_id>\d+)/$', 'get', {
        'queryset': Subject.objects.all(), 
        'template_name': 'get_subjectmodality.html',
        'template_object_name': 'subjectmodality',
        'acl_handler': crud_acl_handler("cursus"),
    }, 'get_subjectmodality'),

    # -- Cursuses ----------------------------------------

    (r'^cursuses/add/$', 'create', {
        'model': Cursus, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_cursuses', 
        'acl_handler': crud_acl_handler("cursus"),
    }, 'add_cursus'),

    (r'^cursuses/(?P<object_id>\d+)/update/$', 'update', {
        'model': Cursus, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'pedagogy:list_cursuses', 
        'acl_handler': crud_acl_handler("cursus"),
    }, 'update_cursus'),

    (r'^cursuses/$', 'list', {
        'model': Cursus, 
        'form_class': CursusForm, 
        'fields': [
            ('Cursus','name'), 
            ('Classes', 'classgroup_set.count')
        ],
        'acl_handler': crud_acl_handler("cursus"),
        'template': 'list_cursuses.html'
    }, 'list_cursuses'),

    (r'^cursuses/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': Cursus,
        'post_delete_redirect': 'pedagogy:list_cursuses',
        'acl_handler': crud_acl_handler("cursus"),
    }, 'delete_cursus'),
    
    (r'^cursuses/(?P<object_id>\d+)/$', 'get', {
        'queryset': Cursus.objects.all(), 
        'template_name': 'get_cursus.html',
        'template_object_name': 'cursus',
        'acl_handler': crud_acl_handler("cursus"),
    }, 'get_cursus'),
)

# Specific views
urlpatterns += patterns('pedagogy.views',
    (r'^studyperiods/(?P<studyperiod_id>\d+)$', 'get_studyperiod', {}, 'get_studyperiod'),
)
