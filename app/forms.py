from django import forms
from .models import *
from django.forms.widgets import Textarea, TextInput, EmailInput

class ContactForm(forms.ModelForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'textbox','placeholder':'Your name'}))
    email = forms.EmailField(widget=EmailInput(attrs={'class':'textbox','placeholder':'Your email'}))
    message = forms.CharField(widget=Textarea(attrs={'placeholder': 'Please enter your subjects'}))
    class Meta:
        model = tbl_contact
        fields = ["username","email","message"]