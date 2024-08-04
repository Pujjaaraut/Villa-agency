from django import forms
from django.contrib.auth.models import User
from .models import MyModel

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','email','first_name','last_name')



class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields =['name','age']