# class base home view
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from memberships.models import MembershipPlans


class HomeView(ListView):
    template_name = "memberships/home.html"
    model = MembershipPlans
    context_object_name = "membershipPlans"
    

class PlanDetailView(DetailView):
    template_name = "memberships/plan_detail.html"
    model = MembershipPlans
    context_object_name = "membershipPlan"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class PlansView(ListView):
    template_name = "memberships/plans.html"
    model = MembershipPlans
    context_object_name = "membershipPlans"
    
    

