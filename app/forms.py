from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = tbl_contact
        fields = ["username","email","message"]