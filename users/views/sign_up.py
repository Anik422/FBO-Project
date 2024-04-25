from users.forms.sign_up_form import SignUpForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages




class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "users/sign_up.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully")
            return redirect("users:sign_in")
        # print(form.first_name)
        return render(request, "users/sign_up.html", {"form": form})