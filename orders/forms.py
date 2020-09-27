from django import forms
from .models import *


class CheckoutContactForm(forms.Form):
    name = forms.CharField(max_length=25, required=True)
    phone = forms.CharField(max_length=25, required=True)
