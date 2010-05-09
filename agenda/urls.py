from django.conf.urls.defaults import *

urlpatterns = patterns('agenda.views.locations',
    (r'^universities/add/$', 'add_university', {}, 'add_university'),
    (r'^universities/$', 'list_universities', {}, 'list_universities'),
    (r'^universities/(?P<university_id>\d+)/delete/$', 
        'delete_university', {}, 'delete_university'),
)

urlpatterns += patterns('agenda.views.pedagogy',
    (r'^cursuses/add/$', 'add_cursus', {}, 'add_cursus'),
    (r'^cursuses/$', 'list_cursuses', {}, 'list_cursuses'),
    (r'^cursuses/(?P<cursus_id>\d+)/delete/$',
       'delete_cursus', {}, 'delete_cursus'),
)
