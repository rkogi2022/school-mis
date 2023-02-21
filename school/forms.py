from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
 
class addattendanceform(ModelForm):
    class Meta:
        model=attendance
        fields="__all__"
 
class addmarksform(ModelForm):
    class Meta:
        model=marks
        fields="__all__"
 
class addnoticeform(ModelForm):
    class Meta:
        model=notice
        fields="__all__"