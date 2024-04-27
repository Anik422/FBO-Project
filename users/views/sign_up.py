from users.forms.sign_up_form import SignUpForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from users.helper import activateEmail
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from users.tokens import account_activation_token




class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "users/sign_up.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get("email"))
            return redirect("users:sign_in")
        return render(request, "users/sign_up.html", {"form": form})

class ActivateView(View):
    def get(self, request, uidb64, token):
        User = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as e:
            user = None
        
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Account activated successfully.")
            return redirect("users:sign_in")
        else:
            messages.error(request, "Activation link is invalid.")
            return redirect("users:sign_in")

