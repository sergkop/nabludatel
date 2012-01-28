from django import forms

from captcha.fields import CaptchaField

from observers.models import Observer

class ObserverSignupForm(forms.ModelForm):
    email = forms.CharField(max_length=50, required=False)
    info = forms.CharField(required=False, widget=forms.Textarea())
    #in_moscow = forms.BooleanField(required=False)
    #captcha = CaptchaField()

    class Meta:
        model = Observer
        exclude = ('in_moscow',)
