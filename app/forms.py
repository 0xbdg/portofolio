from django import forms
from .models import *
from django.forms.widgets import Textarea, TextInput, EmailInput

class ContactForm(forms.ModelForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500',"name":"username",'placeholder':'Your name'}))
    email = forms.EmailField(widget=EmailInput(attrs={'class':'w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500',"name":"email",'placeholder':'Your email'}))
    message = forms.CharField(widget=Textarea(attrs={"class":"w-full px-3 py-2 border rounded-md text-gray-700 focus:outline-none focus:border-blue-500","name":"subject",'placeholder': 'Please enter your subjects'}))
    class Meta:
        model = Feedback
        fields = ["username","email","message"]