# coding=utf8
from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from observers.forms import ObserverSignupForm

def signup(request):
    if request.POST:
        form = ObserverSignupForm(request.POST)

        if form.is_valid():
            observer = form.save(commit=False)
            observer.in_moscow = request.POST.get('in_moscow', 'yes')=='yes'
            observer.save()

            if observer.in_moscow:
                email = settings.MOSCOW_OBSERVERS_EMAIL
            else:
                email = settings.REGION_OBSERVERS_EMAIL

            message = u'ФИО: ' + observer.full_name + '\n'
            message += u'Телефон: ' + observer.telephone + '\n'
            message += u'Адрес: ' + observer.location + '\n'
            message += u'Email: ' + observer.email + '\n'
            message += u'Дополнительно: ' + observer.info + '\n'

            try:
                send_mail(u'Новый наблюдатель', message, 'gn@nabludatel.org', [email], fail_silently=False)
            except SMTPException:
                pass # TODO: write observer id to a special file

            return HttpResponseRedirect('/spasibo/')
    else:
        form = ObserverSignupForm()

    context = {'form': form}
    return render_to_response('signup.html',  context_instance=RequestContext(request, context))
