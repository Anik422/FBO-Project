# create user sign in view class based view
from django.shortcuts import render, redirect
from django.views import View
from users.forms.sign_in_form import SignInForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from users.helper import is_safe_url




class SignInView(View):
    def get(self, request):
        form = SignInForm()
        return render(request, "users/sign_in.html", {"form": form})
    
    

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "User logged in successfully!")
                next_url = request.POST.get('next') 
                if next_url:
                    if is_safe_url(next_url, request.get_host()):
                        return redirect(next_url)
                    else:
                        return redirect("memberships:home")
                else:
                    return redirect("memberships:home")
        return render(request, "users/sign_in.html", {"form": form})