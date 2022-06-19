from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm,widgets
from django import forms
from .models import Profile,Neighbourhood,Business
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']
        
        
class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		exclude = ['user']
		widgets = {
            'fullname': forms.TextInput(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control'}),
        }
class NeighbourhoodForm(ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['area_admin']
        
class BusinessForm(ModelForm):
    class Meta:
        model = Business
        exclude = ['user']