# class base home view
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from memberships.models import MembershipPlans, MembershipServices, Pricing




class HomeView(ListView):
    template_name = "memberships/home.html"
    model = MembershipPlans
    context_object_name = "membershipPlans"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        membershipServices = MembershipServices.objects.all()
        context["title"] = "Home"
        context["membershipServices"] = membershipServices
        return context


class PlanDetailView(DetailView):
    template_name = "memberships/plan_detail.html"
    model = MembershipPlans
    context_object_name = "membershipPlan"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pricings = Pricing.objects.filter(membership_plan=self.object)
        context["title"] = "Plan Detail"
        context["pricings"] = pricings
        return context


class PackageView(ListView):
    template_name = "memberships/PACKAGE.html"
    model = MembershipPlans
    context_object_name = "membershipPlans"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        membershipServices = MembershipServices.objects.all()
        context["title"] = "Home"
        context["membershipServices"] = membershipServices
        return context