from django.conf.urls.defaults import *

urlpatterns = patterns('events.views',
    (r'^$', 'display_calendar', {}, 'display_calendar'),
    (r'^users/me/$', 'get_planning', {'what' : 'me'}, 'get_own_planning'),
    (r'^test/$', 'get_planning', {'what' : 'test'}, 'get_test_planning'),

    #(r'^users/(?P<user_id>\d+)$', 'get_planning', {'what' : 'user'}, 'get_user_planning'),
    (r'^user/add/$', 'add_user_event', {}, 'add_user_event'),
    (r'^move/(?P<when_id>\d+)?$', 'move_event', {}, 'move_event'),
    (r'^resize/(?P<when_id>\d+)?$', 'resize_event', {}, 'resize_event'),
    
    (r'^get/(?P<what>\w+)?(/?(?P<what_arg>\d+)?)?$', 'get_planning', {}, 'get_planning'),
    (r'^ical/(?P<what>\w+)?(/?(?P<what_arg>\d+)?)?$', 'get_ical', {}, 'get_ical'),
    (r'^add/(?P<what>\w+)?(/?(?P<what_arg>\d+)?)?$', 'add_event', {}, 'add_event'),
    (r'^update/(?P<when_id>\d+)?$', 'update_event', {}, 'update_event'),
    (r'^delete/(?P<when_id>\d+)?$', 'delete_event', {}, 'delete_event'),

)
