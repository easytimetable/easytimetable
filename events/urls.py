from django.conf.urls.defaults import *

urlpatterns = patterns('events.views',
    (r'^$', 'display_calendar', {}, 'display_calendar'),
    (r'^users/me/$', 'get_planning', {'what' : 'me'}, 'get_own_planning'),
    (r'^test/$', 'get_planning', {'what' : 'test'}, 'get_test_planning'),
    (r'^get/(?P<what>\w+)?$', 'get_planning', {}, 'get_planning'),
    (r'^users/(?P<user_id>\d+)$', 'get_planning', {'what' : 'user'}, 'get_user_planning'),
    (r'^user/add/$', 'add_user_event', {}, 'add_user_event'),
    (r'^user/move/(?P<when_id>\d+)?$', 'move_user_event', {},
    'move_user_event'),
)