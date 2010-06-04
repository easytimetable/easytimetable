from django.conf.urls.defaults import *

urlpatterns = patterns('locations.views',
    (r'^universities/add/$', 'add_university', {}, 'add_university'),
    (r'^universities/$', 'list_universities', {}, 'list_universities'),
    (r'^universities/(?P<university_id>\d+)/delete/$', 'delete_university', {}, 'delete_university'),
    (r'^universities/(?P<university_id>\d+)$', 'get_university', {}, 'get_university'),
    (r'^universities/(?P<university_id>\d+)/update/$', 'update_university', {}, 'update_university'),
   
    (r'^campuses/add/$', 'add_campus', {}, 'add_campus'),
    (r'^campuses/$', 'list_campuses', {}, 'list_campuses'),
    (r'^campuses/(?P<campus_id>\d+)$', 'get_campus', {}, 'get_campus'),
    (r'^campuses/(?P<campus_id>\d+)/delete/$', 'delete_campus', {}, 'delete_campus'),
    (r'^campuses/(?P<campus_id>\d+)/update/$', 'update_campus', {}, 'update_campus'),

    (r'^places/add/$', 'add_place', {}, 'add_place'),
    (r'^places/$', 'list_places', {}, 'list_places'),
    (r'^places/(?P<place_id>\d+)$', 'get_place', {}, 'get_place'),
    (r'^places/(?P<place_id>\d+)/delete/$', 'delete_place', {}, 'delete_place'),
    (r'^places/(?P<place_id>\d+)/update/$', 'update_place', {}, 'update_place'),
)
