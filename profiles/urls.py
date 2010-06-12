from django.conf.urls.defaults import *
from profiles.models import User

from profiles.models import ClassGroup, Profile
from profiles.forms import StudentForm, CampusManagerForm, TeacherForm
from acls import crud_acl_handler

urlpatterns = patterns('utils.crud',
    
    # -- Classes ----------------------------------------
    
    (r'^classes/(?P<object_id>\d+)/update/$', 'update', {
        'model': ClassGroup, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'profiles:list_classgroups', 
        'acl_handler': crud_acl_handler("campus"),
    }, 'update_classgroup'),

    (r'^classes/$', 'list', {
        'model': ClassGroup, 
        'fields': [('id', 'id'), ('name', 'name')],
        'acl_handler': crud_acl_handler("campus"),
    }, 'list_classgroups'),

    (r'^classes/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': ClassGroup,
        'post_delete_redirect': 'profiles:list_classgroups',
        'acl_handler': crud_acl_handler("campus"),
    }, 'delete_classgroup'),

    (r'^classes/(?P<object_id>\d+)/$', 'get', {
        'queryset': ClassGroup.objects.all(), 
        'template_name': 'get_classgroup.html',
        'template_object_name': 'classgroup',
        'acl_handler': crud_acl_handler("campus"),
    }, 'get_classgroup'),

    # -- Students ---------------------------------------
    
    (r'^students/add/$', 'create', {
        'model': User,
        'form_class': StudentForm,
        'template_name': 'crud/add.html',
        'post_save_redirect': 'profiles:list_students', 
        'acl_handler': crud_acl_handler("campus"),
    }, 'add_student'),
    
    (r'^students/$', 'list', {
        'queryset': User.objects.filter(profile__classgroup__isnull=False),
        'form_class': StudentForm,
        'fields': [
            ('Name', 'username'), 
            ('Class', 'profile_set.get.classgroup.name')],
        'acl_handler': crud_acl_handler("campus"),
        'object_name': 'student', 
        'app_name': 'profiles',
        'rights':{'update': False},
    }, 'list_students'),

    (r'^students/(?P<object_id>\d+)/$', 'get', {
        'queryset': User.objects.filter(profile__classgroup__isnull=False),
        'template_name': 'get_student.html',
        'template_object_name': 'student',
        'acl_handler': crud_acl_handler("campus"),
    }, 'get_student'),
    
    (r'^student/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': User,
        'post_delete_redirect': 'profiles:list_students',
        'acl_handler': crud_acl_handler("campus"),
    }, 'delete_student'),

    # -- Campus Manager -----------------------------------------------
    
    (r'^campus_managers/add/$', 'create', {
        'model': User,
        'form_class': CampusManagerForm,
        'template_name': 'crud/add.html',
        'post_save_redirect': 'profiles:list_campus_managers', 
        'acl_handler': crud_acl_handler("university"),
    }, 'add_campus_manager'),
    
    (r'^campus_managers/$', 'list', {
        'queryset': User.objects.filter(profile__campus_managed__isnull=False).distinct(),
        'form_class': CampusManagerForm,
        'fields':[
            ('First name', 'get_profile.first_name'), 
            ('Last name', 'get_profile.last_name'),
            ('Managed campuses', 'get_profile.list_managed_campuses')],
        'object_name': 'campus_manager',
        'object_verbose_name': 'campus manager',
        'app_name': 'profiles',
        'acl_handler': crud_acl_handler("university"),
        'rights':{'update': False},
    }, 'list_campus_managers'),

    (r'^campus_managers/(?P<object_id>\d+)/$', 'get', {
        'queryset': User.objects.filter(profile__campus_managed__isnull=False).distinct(),
        'template_name': 'get_campus_manager.html',
        'template_object_name': 'campus_manager',
        'acl_handler': crud_acl_handler("university"),
    }, 'get_campus_manager'),

    # -- Teachers ----------------------------------------------------
    
    (r'^teachers/add/$', 'create', {
        'model': User,
        'form_class': TeacherForm,
        'template_name': 'crud/add.html',
        'post_save_redirect': 'profiles:list_teachers', 
        'acl_handler': crud_acl_handler("campus"),
    }, 'add_teacher'),
    
    (r'^teachers/$', 'list', {
        'queryset': User.objects.filter(profile__is_teacher=True),
        'form_class': TeacherForm,
        'fields':[
            ('First name', 'get_profile.first_name'), 
            ('Last name', 'get_profile.last_name')],
        'object_name': 'teacher',
        'object_verbose_name': 'teacher',
        'app_name': 'profiles',
        'acl_handler': crud_acl_handler("campus"),
        'rights':{'update': False, 'view': False},
    }, 'list_teachers'),

    (r'^teachers/(?P<object_id>\d+)/$', 'get', {
        'queryset': User.objects.filter(profile__is_teacher=True),
        'template_name': 'get_teacher.html',
        'template_object_name': 'teacher',
        'acl_handler': crud_acl_handler("campus"),
    }, 'get_teacher'),

    (r'^teacher/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': User,
        'post_delete_redirect': 'profiles:list_teachers',
        'acl_handler': crud_acl_handler("campus"),
    }, 'delete_teacher'),

    # -- All users ---------------------------------------------
    (r'^users/$', 'list', {
        'model': User,
        'form_class': CampusManagerForm,
        'fields':[
            ('First name', 'first_name'), 
            ('Last name', 'last_name'),
            ('Managed campuses', 'get_profile.list_managed_campuses')],
        'object_name': 'user',
        'object_verbose_name': 'User',
        'app_name': 'profiles',
        'acl_handler': crud_acl_handler("university"),
        'rights':{'update': False, 'create': False, 'view': False, 'delete': False},
    }, 'list_users'),
)

# specific views
urlpatterns += patterns('profiles.views',
    (r'^classes/(?P<classgroup_id>\d+)/subjects/$', 'list_classgroup_subjects',{}, 
        'list_classgroup_subjects'),

    # specific because it can add to a specific campus
    (r'^classes/add/$', 'add_classgroup', {}, 'add_classgroup'),
    (r'^classes/add/to_campus/(?P<campus_id>\d+)$', 'add_classgroup',
    {}, 'add_classgroup_to_campus'),
    
    # needed because we don't want to delete cascade all.
    (r'^campus_managers/(?P<user_id>\d+)/delete/$', 'delete_campus_manager', {}, 'delete_campus_manager'),
)
