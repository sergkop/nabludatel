from django.conf.urls.defaults import *

urlpatterns = patterns('observers.views',
    url(r'^stat-nablyudatelem/$', 'signup', name='signup'),
)
