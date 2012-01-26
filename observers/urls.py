from django.conf.urls.defaults import *

urlpatterns = patterns('observers.views',
    url(r'^signup/$', 'signup', name='signup'),
)
