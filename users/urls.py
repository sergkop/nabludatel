from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'profile', name='profile'),
    url(r'^complete_registration/$', 'users.views.complete_registration', name='complete_registration'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
