from django.conf.urls.defaults import *

urlpatterns = patterns('events.views',
    (r'^$', 'display_calendar', {}, 'display_calendar'),
    (r'^users/me/$', 'get_planning', {'what' : 'me'}, 'get_own_planning'),
    (r'^test/$', 'get_planning', {'what' : 'test'}, 'get_test_planning'),
    (r'^get/(?P<what>\w+)?(/?(?P<what_arg>\d+))?$', 'get_planning', {}, 'get_planning'),

    (r'^users/(?P<user_id>\d+)$', 'get_planning', {'what' : 'user'}, 'get_user_planning'),
    (r'^user/add/$', 'add_user_event', {}, 'add_user_event'),
    (r'^move/(?P<when_id>\d+)?$', 'move_event', {},
    'move_event'),
    (r'^update/(?P<when_id>\d+)?$', 'update_event', {},
    'update_event'),
    
    (r'^campus_manager/$', 'display_campus_mgr_calendar', {},
    'display_campus_mgr_calendar'),
    (r'^campus_manager/campus/add/$', 'add_campus_event', {}, 'add_campus_event'),
    (r'^campus_manager/class/add/$', 'add_classgroup_event', {}, 
                                     'add_classgroup_event'),
)
