from django.conf.urls.defaults import *
from locations.forms import CampusForm
from locations.models import University, Campus, Place 

urlpatterns = patterns('utils.crud',

    # -- Universities ----------------------------------------
    (r'^universities/add/$', 'create', {
        'model': University, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'locations:list_universities', 
    }, 'add_university'),

    (r'^universities/(?P<object_id>\d+)/update/$', 'update', {
        'model': University, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'locations:list_universities', 
    }, 'update_university'),

    (r'^universities/$', 'list', {
        'model': University, 
        'fields': [('University', 'name'), ('Campus', 'campus_set.count')],
    }, 'list_universities'),

    (r'^universities/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': University,
        'post_delete_redirect': 'locations:list_universities'
    }, 'delete_university'),

    (r'^universities/(?P<object_id>\d+)/$', 'get', {
        'queryset': University.objects.all(), 
        'template_name': 'get_university.html',
        'template_object_name': 'university',
    }, 'get_university'),

    # -- Campuses ------------------------------------------------
    (r'^campuses/add/$', 'create', {
        'form_class': CampusForm, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'locations:list_campuses', 
    }, 'add_campus'),

    (r'^campuses/(?P<object_id>\d+)/update/$', 'update', {
        'form_class': CampusForm, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'locations:list_campuses', 
    }, 'update_campus'),

    (r'^campuses/$', 'list', {
        'model': Campus,
        'form_class': CampusForm,
        'fields': [('Campus', 'name'), ('University', 'university.name')],
    }, 'list_campuses'),

    (r'^campuses/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': Campus,
        'post_delete_redirect': 'locations:list_campuses'
    }, 'delete_campus'),

    (r'^campuses/(?P<object_id>\d+)/$', 'get', {
        'queryset': Campus.objects.all(), 
        'template_name': 'get_campus.html',
        'template_object_name': 'campus',
    }, 'get_campus'),

    # -- Places ------------------------------------------------
    (r'^places/add/$', 'create', {
        'model': Place, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'locations:list_places', 
    }, 'add_place'),

    (r'^places/(?P<object_id>\d+)/update/$', 'update', {
        'model': Place, 
        'template_name': 'crud/add.html',
        'post_save_redirect': 'locations:list_places', 
    }, 'update_place'),

    (r'^places/$', 'list', {
        'model': Place,
        'fields': [('Id','id'),('Text', 'name')],
    }, 'list_places'),

    (r'^places/(?P<object_id>\d+)/delete/$', 'delete', {
        'model': Place,
        'post_delete_redirect': 'locations:list_places'
    }, 'delete_place'),

    (r'^places/(?P<object_id>\d+)/$', 'get', {
        'queryset': Place.objects.all(), 
        'template_name': 'get_place.html',
        'template_object_name': 'place',
    }, 'get_place'),
)
