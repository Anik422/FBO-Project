#forgot password form
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class ForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        User = get_user_model()
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user found with this email.")
        return email

    
class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
    )
    confirm_password = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password does not match.")
        return cleaned_data