from django import forms
import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget

from .models import blog, Author




class PostForm(forms.ModelForm):

	class Meta:
		model = blog
		fields = ('title', 'body',)

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	date_of_birth = forms.DateField(widget = forms.SelectDateWidget(years=range(1900, datetime.date.today().year)),)
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'date_of_birth', 'email', 'password1', 'password2', )
