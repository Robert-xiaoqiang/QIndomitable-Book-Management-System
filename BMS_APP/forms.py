from django import forms
from .models import *

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['user_id', 'user_name', 'pass_word']
		labels = {'user_id': 0, 'user_name': '', 'pass_word': ''}

class ReaderForm(forms.ModelForm):
	class Meta:
		model = Reader
		fields = ['reader_id', 'name', 'user', 'address', 'occupation', 'email']
		labels = {'reader_id': 0, 'name': '', 'user': '', 'address': '', 'occupation': '', 'email': ''}
