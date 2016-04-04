from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from gp.models import Domain
from gp.methods import get_list_of_domains

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input', 'id':'username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input', 'id':'password'}))
	

class postComplaintForm(forms.Form):
	domain = forms.ChoiceField(choices = get_list_of_domains(), widget=forms.RadioSelect(attrs={'class':'mdl-radio__button'}))
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input'}))
	hostel = forms.ChoiceField(label='',choices = (('gh','Girls Hostel'),('bh','Boys Hostel')),widget=forms.RadioSelect(attrs={'class':'mdl-radio__button','id':'radio-hostel'}))
	description = forms.CharField(widget = forms.Textarea(attrs={'class':'mdl-textfield__input','rows':'5'}))

class emailForm(forms.Form):
	recepients = forms.CharField(widget= forms.TextInput(attrs={'class':'mdl-textfield__input'}))
	body = forms.CharField(widget = forms.Textarea(attrs={'class':'mdl-textfield__input','rows':'5'}))

