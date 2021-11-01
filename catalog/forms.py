import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
#from .forms import RenewBookForm
from .models import BookInstance
from django.forms import ModelForm
from .models import BookInstance
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
    name = forms.CharField(label='name', max_length=30)
    email = forms.EmailField(label='E-mail')
    inquiry = forms.CharField(label='Feel free to ask any questions', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        inquiry = self.cleaned_data['inquiry']

        message = EmailMessage(subject=name + "からの問い合わせ",
                               body=inquiry,
                               from_email=email,
                               to=["fr8ybzthb@icloud.com"],
                               cc=[email])
        message.send()