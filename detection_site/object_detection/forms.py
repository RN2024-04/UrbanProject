from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth.models import User
from object_detection.models import PeopleReg


class LoginForm (AuthenticationForm):
    username=forms.CharField()
    password = forms.CharField()


class UserRegisterForm (UserCreationForm):
    username = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password'],
            self.cleaned_data["password2"]
        )
        if commit:
            user.save()
        return user


# class RegisterForm (UserCreationForm):
#     username=forms.CharField()
#     password = forms.CharField()
#     password2 = forms.CharField()
#
#     def save(self, commit=True):
#         user = super(RegisterForm, self).save(commit=False)
#         user.username = self.cleaned_data["username"]
#         user.password = self.cleaned_data["password"]
#         user.password2 = self.cleaned_data["password2"]
#         if commit:
#             user.save()
#         return user
