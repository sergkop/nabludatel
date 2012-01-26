from django.forms import ModelForm

from captcha.fields import CaptchaField

from observers.models import Observer

class ObserverSignupForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Observer
