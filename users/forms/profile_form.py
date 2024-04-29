from django import forms
from users.models import CustomUser
from django.core.validators import EmailValidator


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Firstname', 'class': 'w-full p-2 border border-gray-300 rounded-md placeholder:font-light'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Lastname', 'class': 'w-full p-2 border border-gray-300 rounded-md placeholder:font-light'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'User Name', 'class': 'w-full p-2 border border-gray-300 rounded-md'}))
    email = forms.CharField(max_length=100, validators=[EmailValidator()], widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'w-full p-2 border border-gray-300 rounded-md', 'readonly': True, 'disabled': True}))
    
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "email"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "username": "Username",
            "email": "Email",
        }
        