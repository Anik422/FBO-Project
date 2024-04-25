#create user sign in form
from django import forms
from users.models import CustomUser
from django.core.exceptions import ValidationError


class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not CustomUser.objects.filter(username=username).exists():
            raise ValidationError("User does not exist!")

        user = CustomUser.objects.get(username=username)
        if not user.check_password(password):
            raise ValidationError("Password is incorrect!")
