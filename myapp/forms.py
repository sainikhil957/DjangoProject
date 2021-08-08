from django import forms
from .models import Fdsignup
from .models import Cusignup
from .models import Fdform

class fdsignupform(forms.ModelForm):
    class Meta:
        model=Fdsignup
        fields="__all__"


class cusignupform(forms.ModelForm):
    class Meta:
        model=Cusignup
        fields="__all__"

class fdform(forms.ModelForm):
    class Meta:
        model=Fdform
        fields="__all__"
