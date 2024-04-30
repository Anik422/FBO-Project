#forgot password view
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordChangeDoneView
from django.urls import reverse
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from users.forms.forgot_password_form import ForgotPasswordForm, ResetPasswordForm
from django.contrib import messages


class ForgotPasswordView(PasswordResetView):
    template_name = "users/forgot_password.html"
    form_class = ForgotPasswordForm
    email_template_name = "users/password_reset_email.html"
    success_url = reverse_lazy("users:password_reset_done")
    subject_template_name = "users/password_reset_subject.txt"
    token_generator = default_token_generator

    def form_valid(self, form):
        messages.success(self.request, "Password reset email has been sent. Please check your inbox.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error submitting password reset request. Please try again.")
        return super().form_invalid(form)
    
class ResetPasswordEmailDoneView(PasswordChangeDoneView):
    template_name = "users/password_reset_done.html"
    


class ResetPasswordView(PasswordResetConfirmView):
    template_name = "users/reset_password.html"
    success_url = reverse_lazy("users:password_reset_done")
    reset_url_token = "password_reset_confirm"
    
    def form_valid(self, form):
        messages.success(self.request, "Password reset successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Password reset failed. Please try again.")
        return super().form_invalid(form)
 
    