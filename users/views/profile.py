from django.shortcuts import render, redirect
from django.views import View
from users.forms.profile_form import ProfileForm
from users.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        user = request.user
        form = ProfileForm(instance=user)
        return render(request, "users/profile.html", {"form": form})

    def post(self, request):
        user = request.user
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("users:profile")
        else:
            messages.error(request, "There was an error updating your profile.")
        return render(request, "users/profile.html", {"form": form})
