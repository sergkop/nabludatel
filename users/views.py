from django.contrib import messages, auth
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from loginza.models import UserMap
from loginza.templatetags.loginza_widget import _return_path

from users.forms import CompleteRegistrationForm

def profile(request):
    return HttpResponse('test1')

#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
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
