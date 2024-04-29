# create sinout confirmation view and signout view
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

# set login required 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class SignOutConfirmationView(TemplateView):
    template_name = "users/sign_out_confirmation.html"

    def get(self, request):
        return render(request, self.template_name)
    
    
@method_decorator(login_required, name='dispatch')
class SignOutView(TemplateView):
    def post(self, request):
        logout(request)
        messages.success(request, "User logged out successfully!")
        return redirect("users:sign_in")
