from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def profile(request):
    return HttpResponse('test1')
