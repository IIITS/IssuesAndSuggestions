from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from gp.models import Domain
from gp.methods import get_list_of_domains

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input', 'id':'username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input', 'id':'password'}))
	

class PostComplaintForm(forms.Form):
	domain = forms.ChoiceField(choices = get_list_of_domains(), widget=forms.RadioSelect(attrs={'class':'mdl-radio__button','id':'domains'}))
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input','pattern':'.{1,}','required title':'1 character minimum'}))
	hostel = forms.ChoiceField(required=False,label='',choices = (('gh','Girls Hostel'),('bh','Boys Hostel')),widget=forms.RadioSelect(attrs={'class':'mdl-radio__button'}))
	description = forms.CharField(widget = forms.Textarea(attrs={'class':'mdl-textfield__input','rows':'5','pattern':'.{1,}','required title':'1 character minimum'}))

class Email_Form(forms.Form):
	recep = forms.CharField(widget= forms.TextInput(attrs={'class':'mdl-textfield__input'}))
	bod = forms.CharField(label='',widget = forms.Textarea(attrs={'class':'mdl-textfield__input','rows':'5'}))

class SuggestionForm(forms.Form):
	text = forms.CharField(widget= forms.Textarea(attrs={'class':'mdl-textfield__input','rows':'3'}))


	
