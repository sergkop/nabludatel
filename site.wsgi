import settings
import site
# load virtualenv if set
if settings.VIRTUALENV:
    site.addsitedir(settings.VIRTUALENV)


import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
path = os.path.dirname(__file__)
if path not in sys.path:
    sys.path.insert(0, path)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
