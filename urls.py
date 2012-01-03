from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from cms.sitemaps import CMSSitemap

admin.autodiscover()

# TODO: sitemap doesn't work yet (because of redirect to sitemap.xml/) - see APPEND_SLASH
urlpatterns = patterns('',
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
    (r'^admin/', include(admin.site.urls)),
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    url(r'^', include('navigation.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
