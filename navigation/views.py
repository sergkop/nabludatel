from django.shortcuts import render_to_response
from django.template import RequestContext

from zinnia.models import Entry

def main(request):
    context = {
        'news': Entry.published.all()[:3],
    }
    return render_to_response('main.html', RequestContext(request, context))

def search_results(request):
    return render_to_response('search_results.html', RequestContext(request, {}))
