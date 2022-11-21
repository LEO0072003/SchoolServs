from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Teacher


class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username', 'usertype']


