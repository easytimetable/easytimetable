from django.conf.urls.defaults import *
from locations.forms import CampusForm
from locations.models import University, Campus, Place 
from acls import crud_acl_handler

urlpatterns = patterns('utils.crud',

    # -- Universities ----------------------------------------
    (r'^universities/add/$', 'create', {
        'model': University, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'locations:list_universities', 
        'acl_handler': crud_acl_handler("university"),
    }, 'add_university'),

    (r'^universities/(?P<object_id>\d+)/update/$', 'update', {
        'model': University, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'locations:list_universities', 
        'acl_handler': crud_acl_handler("university"),
    }, 'update_university'),

    (r'^universities/$', 'list', {
        'model': University, 
        'fields': [
            ('University', 'name'), 
            ('Campus', 'campus_set.count')],
        'acl_handler': crud_acl_handler("university"),
    }, 'list_universities'),

    (r'^universities/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': University,
        'post_delete_redirect': 'locations:list_universities',
        'acl_handler': crud_acl_handler("university"),
    }, 'delete_university'),

    (r'^universities/(?P<object_id>\d+)/$', 'get', {
        'queryset': University.objects.all(), 
        'template_name': 'get_university.html',
        'template_object_name': 'university',
        'acl_handler': crud_acl_handler("university"),
    }, 'get_university'),

    # -- Campuses ------------------------------------------------
    (r'^campuses/add/$', 'create', {
        'form_class': CampusForm, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'locations:list_campuses', 
        'acl_handler': crud_acl_handler("campus"),
    }, 'add_campus'),

    (r'^campuses/(?P<object_id>\d+)/update/$', 'update', {
        'form_class': CampusForm, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'locations:list_campuses', 
        'acl_handler': crud_acl_handler("campus"),
    }, 'update_campus'),

    (r'^campuses/$', 'list', {
        'model': Campus,
        'form_class': CampusForm,
        'fields': [('Campus', 'name'), ('University', 'university.name')],
        'acl_handler': crud_acl_handler("campus"),
        'template': 'list_campus.html'
    }, 'list_campuses'),

    (r'^campuses/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': Campus,
        'post_delete_redirect': 'locations:list_campuses',
        'acl_handler': crud_acl_handler("campus"),
    }, 'delete_campus'),

    (r'^campuses/(?P<object_id>\d+)/$', 'get', {
        'queryset': Campus.objects.all(), 
        'template_name': 'get_campus.html',
        'template_object_name': 'campus',
        'acl_handler': crud_acl_handler("campus"),
    }, 'get_campus'),

    # -- Places ------------------------------------------------
    (r'^places/add/$', 'create', {
        'model': Place, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'locations:list_places', 
        'acl_handler': crud_acl_handler("place"),
    }, 'add_place'),

    (r'^places/(?P<object_id>\d+)/update/$', 'update', {
        'model': Place, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'locations:list_places', 
        'acl_handler': crud_acl_handler("place"),
    }, 'update_place'),

    (r'^places/$', 'list', {
        'queryset': Place.objects.filter(is_main_place=False),
        'fields': [('Place', 'name'), ('Campus','campus.name'), ('Address', 'address')],
        'acl_handler': crud_acl_handler("place"),
        'template': 'list_places.html'
    }, 'list_places'),

    (r'^places/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': Place,
        'post_delete_redirect': 'locations:list_places',
        'acl_handler': crud_acl_handler("place"),
    }, 'delete_place'),

    (r'^places/(?P<object_id>\d+)/$', 'get', {
        'queryset': Place.objects.all(), 
        'template_name': 'get_place.html',
        'template_object_name': 'place',
        'acl_handler': crud_acl_handler("place"),
    }, 'get_place'),
)
