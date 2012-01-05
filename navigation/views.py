from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def main(request):
    path = request.path
    #if path is not None and path not in settings.LOGINZA_AMNESIA_PATHS:
    request.session['loginza_return_path'] = path or 'test'

    return render_to_response('main.html', RequestContext(request, {}))
