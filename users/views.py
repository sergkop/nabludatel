from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.utils import simplejson as json

from loginza.models import Identity, UserMap
from loginza.templatetags.loginza_widget import _return_path

from users.forms import CompleteRegistrationForm
import users.signals

def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('main')) # TODO: redirect to login page

    user_map = UserMap.objects.get(user=request.user) # TODO: what if there are several user maps?
    data = json.loads(user_map.identity.data)

    context = {
        'user_data': data,
    }
    return render_to_response('users/profile.html', context_instance=RequestContext(request, context))

# TODO: what if user has previously logged in with another social network account
def complete_registration(request):
    if request.user.is_authenticated():
        return HttpResponseForbidden('sdfsd') # TODO: redirect

    try:
        identity_id = request.session.get('users_complete_reg_id', None)
        user_map = UserMap.objects.get(identity__id=identity_id)
    except UserMap.DoesNotExist:
        return HttpResponseForbidden('sdf')

    if request.method == 'POST':
        form = CompleteRegistrationForm(user_map.user.id, request.POST)
        if form.is_valid():
            user_map.user.username = form.cleaned_data['username']
            user_map.user.email = form.cleaned_data['email']
            user_map.user.save()

            user_map.verified = True
            user_map.save()

            user = auth.authenticate(user_map=user_map)
            auth.login(request, user)

            messages.info(request, u'Welcome!')
            del request.session['users_complete_reg_id']
            return redirect(_return_path(request))
    else:
        form = CompleteRegistrationForm(user_map.user.id, initial={
                'username': user_map.user.username,
                'email': user_map.user.email,
        })

    return render_to_response('users/complete_reg.html', {'form': form},
            context_instance=RequestContext(request))
