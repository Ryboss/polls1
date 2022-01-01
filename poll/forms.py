from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import ResultsModel
from django import forms

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')

class ResultsForm(forms.ModelForm):
    class Meta:
        model = ResultsModel
        fields =('answer',)