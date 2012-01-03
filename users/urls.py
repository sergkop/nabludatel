from django.conf.urls.defaults import *

urlpatterns = patterns('users.views',
    url(r'^qwe$', 'profile', name='profile'),
)
