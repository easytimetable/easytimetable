from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',
    (r'^classes/add/$', 'add_classgroup', {}, 'add_classgroup'),
    (r'^classes/$', 'list_classgroups', {}, 'list_classgroups'),
    (r'^classes/(?P<classgroup_id>\d+)$', 'get_classgroup', {}, 'get_classgroup'),
    (r'^classes/(?P<classgroup_id>\d+)/delete/$', 'delete_classgroup', {}, 'delete_classgroup'),
    (r'^classes/(?P<classgroup_id>\d+)/update/$', 'update_classgroup', {}, 'update_classgroup'),

    (r'^students/add/$', 'add_student', {}, 'add_student'),
    (r'^students/$', 'list_students', {}, 'list_students'),
    (r'^students/(?P<student_id>\d+)$', 'get_student', {}, 'get_student'),
    (r'^students/(?P<student_id>\d+)/delete/$', 'delete_student', {}, 'delete_student'),
    (r'^students/(?P<student_id>\d+)/update/$', 'update_student', {}, 'update_student'),
)
