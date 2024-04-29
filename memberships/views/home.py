# class base home view
from django.views.generic import TemplateView
from django.shortcuts import render, redirect


class HomeView(TemplateView):
    template_name = "memberships/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
