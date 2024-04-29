#forgot password form
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator


class ForgotPasswordForm(PasswordResetForm):
    email = forms.CharField(max_length=100, validators=[EmailValidator()], widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'w-full p-2 border border-gray-300 rounded-md'}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        User = get_user_model()
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user found with this email.")
        return email

    
class ResetPasswordForm(forms.Form):
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={"class": "w-full p-2 border border-gray-300 rounded-md placeholder:font-light placeholder:text-gray-500"})
    )
    new_password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "w-full p-2 border border-gray-300 rounded-md placeholder:font-light placeholder:text-gray-500"})
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")
        if new_password1 != new_password2:
            raise forms.ValidationError("The passwords do not match.")
        return cleaned_data
