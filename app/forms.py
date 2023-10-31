from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



class CustomAuthenticationForm(AuthenticationForm):
	class Meta:
		fields=("username","password")
  
  
class QuestionForm(forms.ModelForm):
	class Meta:
		model=Question
		fields="__all__"
  
class AnswerForm(forms.ModelForm):
	class Meta:
		model=Answer
		fields=("answer",)