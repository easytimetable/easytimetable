from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',
    (r'^classes/add/$', 'add_classgroup', {}, 'add_classgroup'),
    (r'^classes/add/to_campus/(?P<campus_id>\d+)$', 'add_classgroup',
    {}, 'add_classgroup_to_campus'),

    (r'^classes/$', 'list_classgroups', {}, 'list_classgroups'),
    (r'^classes/(?P<classgroup_id>\d+)$', 'get_classgroup', {}, 'get_classgroup'),
    (r'^classes/(?P<classgroup_id>\d+)/delete/$', 'delete_classgroup', {}, 'delete_classgroup'),
    (r'^classes/(?P<classgroup_id>\d+)/update/$', 'update_classgroup', {}, 'update_classgroup'),
    (r'^classes/(?P<classgroup_id>\d+)/subjects/$', 'list_classgroup_subjects',
    {}, 'list_classgroup_subjects'),

    (r'^users/(?P<user_id>\d+)/delete/$', 'delete_user', {}, 'delete_user'),

    (r'^students/add/$', 'add_student', {}, 'add_student'),
    (r'^students/$', 'list_students', {}, 'list_students'),
    (r'^students/(?P<student_id>\d+)$', 'get_student', {}, 'get_student'),
    (r'^students/(?P<student_id>\d+)/update/$', 'update_student', {}, 'update_student'),

    (r'^campus_managers/add/$', 'add_campus_manager', {}, 'add_campus_manager'),
    (r'^campus_managers/$', 'list_campus_managers', {}, 'list_campus_managers'),
    (r'^campus_managers/(?P<campus_manager_id>\d+)$', 'get_campus_manager', {}, 'get_campus_manager'),
    (r'^campus_managers/(?P<campus_manager_id>\d+)/update/$', 'update_campus_manager', {}, 'update_campus_manager'),
)
