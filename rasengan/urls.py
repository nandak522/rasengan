from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'versions.views.view_enter_versions', {'enter_versions_template':'enter_versions.html'}, name='home'),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^users/', include('users.urls')),
    url(r'^versions/', include('versions.urls')),
)
