from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    (r'^$', 'django.views.generic.simple.direct_to_template', {
        'template': 'index.html',
    }, 'index'),
    (r'^doc/$', 'django.views.generic.simple.direct_to_template', {
        'template': 'doc_commerciale.html',
    }, 'index'),
    (r'^admin/', include(admin.site.urls)),
    (r'^pedagogy/', include('pedagogy.urls', namespace='pedagogy')),
    (r'^events/', include('events.urls', namespace='events')),
    (r'^locations/', include('locations.urls', namespace='locations')),
    (r'^profiles/', include('profiles.urls', namespace='profiles')),
    
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {}, 'login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {}, 'logout'),
)

# To serve static files. Do not use in production
if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('', 
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT}),
    )
