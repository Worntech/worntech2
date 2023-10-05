from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class MyUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'username', 'phone']

class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        #fields= ["name", "details", "image"]
        
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        
class ProjectorderForm(ModelForm):
    class Meta:
        model = Projectorder
        fields = '__all__'
        
class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'