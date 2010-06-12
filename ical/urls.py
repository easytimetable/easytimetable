from django.conf.urls.defaults import *


urlpatterns = patterns('ical.views',
    (r'^$', 'display_ical_mgmnt', {}, 'display_ical_mgmnt'),
    (r'^reset/(?P<hash>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$', 'reset_hash', {},
    'reset_hash'),
    (r'^get/(?P<hash>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$',
    'get_feed', {},
    'get_feed'),
)
