from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',
    (r'^classes/add/$', 'add_classgroup', {}, 'add_classgroup'),
    (r'^classes/$', 'list_classgroups', {}, 'list_classgroups'),
    (r'^classes/(?P<classgroup_id>\d+)$', 'get_classgroup', {}, 'get_classgroup'),
    (r'^classes/(?P<classgroup_id>\d+)/delete/$', 'delete_classgroup', {}, 'delete_classgroup'),
    (r'^classes/(?P<classgroup_id>\d+)/update/$', 'update_classgroup', {}, 'update_classgroup'),
)
