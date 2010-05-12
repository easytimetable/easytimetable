from django.conf.urls.defaults import *

urlpatterns = patterns('agenda.views.locations',
    (r'^universities/add/$', 'add_university', {}, 'add_university'),
    (r'^universities/$', 'list_universities', {}, 'list_universities'),
    (r'^universities/(?P<university_id>\d+)/delete/$', 
        'delete_university', {}, 'delete_university'),
    (r'^campuses/add/$', 'add_campus', {}, 'add_campus'),
    (r'^campuses/$', 'list_campuses', {}, 'list_campuses'),
    (r'^campuses/(?P<campus_id>\d+)$', 'get_campus', {}, 'get_campus'),
    (r'^campuses/(?P<campus_id>\d+)/delete/$', 
        'delete_campus', {}, 'delete_campus'),
)

urlpatterns += patterns('agenda.views.pedagogy',
    (r'^cursuses/add/$', 'add_cursus', {}, 'add_cursus'),
    (r'^cursuses/$', 'list_cursuses', {}, 'list_cursuses'),
    (r'^cursuses/(?P<cursus_id>\d+)$', 'get_cursus', {}, 'get_cursus'),
    (r'^cursuses/(?P<cursus_id>\d+)/delete/$',
       'delete_cursus', {}, 'delete_cursus'),
	(r'^studyperiods/add/$', 'add_studyperiod', {}, 'add_studyperiod'),
    (r'^studyperiods/$', 'list_studyperiods', {}, 'list_studyperiods'),
    (r'^studyperiods/(?P<studyperiod_id>\d+)$', 'get_studyperiod', {}, 'get_studyperiod'),
    (r'^studyperiods/(?P<studyperiod_id>\d+)/delete/$',
       'delete_studyperiod', {}, 'delete_studyperiod'),
	(r'^subjects/add/$', 'add_subject', {}, 'add_subject'),
    (r'^subjects/$', 'list_subjects', {}, 'list_subjects'),
    (r'^subjects/(?P<subject_id>\d+)$', 'get_subject', {}, 'get_subject'),
    (r'^subjects/(?P<subject_id>\d+)/delete/$',
       'delete_subject', {}, 'delete_subject'),
)

urlpatterns += patterns('agenda.views.classgroups',
    (r'^classes/add/$', 'add_classgroup', {}, 'add_classgroup'),
    (r'^classes/$', 'list_classgroups', {}, 'list_classgroups'),
    (r'^classes/(?P<classes_id>\d+)$', 'get_classgroup', {}, 'get_classgroup'),
    (r'^classes/(?P<classgroup_id>\d+)/delete/$',
       'delete_classgroup', {}, 'delete_classgroup'),
)
