#forgot password view
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
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
    success_url = reverse_lazy("users:sign_in")
    subject_template_name = "users/password_reset_subject.txt"
    token_generator = default_token_generator


class ResetPasswordView(PasswordResetConfirmView):
    template_name = "users/reset_password.html"
    form_class = ResetPasswordForm
    success_url = reverse_lazy("users:sign_in")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["uidb64"] = self.kwargs.get("uidb64")
        context["token"] = self.kwargs.get("token")
        return context

    def post(self, request, uidb64, token):
        User = get_user_model()
        try:
            uid = urlsafe_base64_encode(force_bytes(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as e:
            user = None

        if user is not None and self.token_generator.check_token(user, token):
            form = self.form_class(request.POST)
            if form.is_valid():
                user.set_password(form.cleaned_data.get("password"))
                user.save()
                messages.success(request, _("Password reset successful."))
                return redirect("users:sign_in")
            return render(request, self.template_name, {"form": form})
        else:
            messages.error(request, _("Password reset link is invalid."))
            return redirect("users:sign_in")