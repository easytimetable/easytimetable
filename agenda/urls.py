from django.conf.urls.defaults import *

urlpatterns = patterns('agenda.views.locations',
    (r'^universities/add/$', 'add_university', {}, 'add_university'),
    (r'^universities/$', 'list_universities', {}, 'list_universities'),
    (r'^universities/(?P<university_id>\d+)/delete/$', 
        'delete_university', {}, 'delete_university'),
)
