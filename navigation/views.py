from django.shortcuts import render_to_response
from django.template import RequestContext

def main(request):
    return render_to_response('main.html', RequestContext(request, {}))

def search_results(request):
    return render_to_response('search_results.html', RequestContext(request, {}))
