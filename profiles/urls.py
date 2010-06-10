from django.conf.urls.defaults import *
from profiles.models import ClassGroup, Profile
from profiles.forms import StudentForm, CampusManagerForm

urlpatterns = patterns('utils.crud',
    
    # -- Classes ----------------------------------------
    (r'^classes/(?P<object_id>\d+)/update/$', 'update', {
        'model': ClassGroup, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'profiles:list_classgroups', 
    }, 'update_classgroup'),

    (r'^classes/$', 'list', {
        'model': ClassGroup, 
        'fields': [('id', 'id'), ('name', 'name')],
    }, 'list_classgroups'),

    (r'^classes/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': ClassGroup,
        'post_delete_redirect': 'profiles:list_classgroups'
    }, 'delete_classgroup'),

    (r'^classes/(?P<object_id>\d+)/$', 'get', {
        'queryset': ClassGroup.objects.all(), 
        'template_name': 'get_classgroup.html',
        'template_object_name': 'classgroup',
    }, 'get_classgroup'),
)

urlpatterns += patterns('profiles.views',
    (r'^classes/add/$', 'add_classgroup', {}, 'add_classgroup'),
    (r'^classes/add/to_campus/(?P<campus_id>\d+)$', 'add_classgroup',
    {}, 'add_classgroup_to_campus'),
    
    (r'^users/(?P<user_id>\d+)/delete/$', 'delete_user', {}, 'delete_user'),
    (r'^users/(?P<user_id>\d+)/delete/$', 'delete_user', {}, 'delete_student'),

    (r'^students/add/$', 'add_student', {}, 'add_student'),
    (r'^students/$', 'list_students', {}, 'list_students'),
    (r'^students/(?P<student_id>\d+)$', 'get_student', {}, 'get_student'),
    (r'^students/(?P<student_id>\d+)/update/$', 'update_student', {}, 'update_student'),

    (r'^campus_managers/add/$', 'add_campus_manager', {}, 'add_campus_manager'),
    (r'^campus_managers/$', 'list_campus_managers', {}, 'list_campus_managers'),
    (r'^campus_managers/(?P<campus_manager_id>\d+)$', 'get_campus_manager', {}, 'get_campus_manager'),
    (r'^campus_managers/(?P<campus_manager_id>\d+)/update/$', 'update_campus_manager', {}, 'update_campus_manager'),
    (r'^campus_managers/(?P<user_id>\d+)/delete/$', 'delete_campus_manager', {}, 'delete_campus_manager'),
)
