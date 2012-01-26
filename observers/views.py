from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from observers.forms import ObserverSignupForm

def signup(request):
    if request.POST:
        form = ObserverSignupForm(request.POST)

        if form.is_valid():
            
            return HttpResponseRedirect('/thank_you/')
    else:
        form = ObserverSignupForm()

    context = {'form': form}
    return render_to_response('signup.html',  context_instance=RequestContext(request, context))
