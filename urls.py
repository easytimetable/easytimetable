from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('agenda.urls', namespace='agenda')),
)

# To serve static files. Do not use in production
if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('', 
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT}),
    )
