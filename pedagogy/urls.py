from django.conf.urls.defaults import *

urlpatterns = patterns('pedagogy.views',
    (r'^cursuses/add/$', 'add_cursus', {}, 'add_cursus'),
    (r'^cursuses/$', 'list_cursuses', {}, 'list_cursuses'),
    (r'^cursuses/(?P<cursus_id>\d+)$', 'get_cursus', {}, 'get_cursus'),
    (r'^cursuses/(?P<cursus_id>\d+)/delete/$', 'delete_cursus', {}, 'delete_cursus'),
    (r'^cursuses/(?P<cursus_id>\d+)/update/$', 'update_cursus', {}, 'update_cursus'),

    (r'^studyperiods/add/$', 'add_studyperiod', {}, 'add_studyperiod'),
    (r'^studyperiods/$', 'list_studyperiods', {}, 'list_studyperiods'),
    (r'^studyperiods/(?P<studyperiod_id>\d+)$', 'get_studyperiod', {}, 'get_studyperiod'),
    (r'^studyperiods/(?P<studyperiod_id>\d+)/delete/$', 'delete_studyperiod', {}, 'delete_studyperiod'),
    (r'^studyperiods/(?P<studyperiod_id>\d+)/update/$', 'update_studyperiod', {}, 'update_studyperiod'),

    (r'^subjects/add/$', 'add_subject', {}, 'add_subject'),
    (r'^subjects/$', 'list_subjects', {}, 'list_subjects'),
    (r'^subjects/(?P<subject_id>\d+)$', 'get_subject', {}, 'get_subject'),
    (r'^subjects/(?P<subject_id>\d+)/delete/$', 'delete_subject', {}, 'delete_subject'),
    (r'^subjects/(?P<subject_id>\d+)/update/$', 'update_subject', {}, 'update_subject'),
       
    (r'^subjectmodalities/add/$', 'add_subjectmodality', {}, 'add_subjectmodality'),
    (r'^subjectmodalities/$', 'list_subjectmodalities', {}, 'list_subjectmodalities'),
    (r'^subjectmodalities/(?P<subjectmodality_id>\d+)$', 'get_subjectmodality', {}, 'get_subjectmodality'),
    (r'^subjectmodalities/(?P<subjectmodality_id>\d+)/delete/$', 'delete_subjectmodality', {}, 'delete_subjectmodality'),
    (r'^subjectmodalities/(?P<subjectmodality_id>\d+)/update/$', 'update_subjectmodality', {}, 'update_subjectmodality'),

)
