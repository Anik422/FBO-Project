from django.http import HttpRequest, HttpResponse
from memberships.models import MembershipPlans, MembershipServices, Pricing, SubscriptionPlan
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class SubscriptionPlanView(CreateView):
    # model = SubscriptionPlan
    # fields = ["membership_plan", "user", "pricing"]
    
    
    def get(self, request: HttpRequest, membershipPlanSlug: str, packageSlug: str) -> HttpResponse:
        membershipPlan = MembershipPlans.objects.get(slug=membershipPlanSlug)
        package = Pricing.objects.get(slug=packageSlug)
        SubscriptionPlan.objects.create(
            membership_plan=membershipPlan,
            user=request.user,
            pricing=package,
        )
        messages.success(request, "Subscription Plan created successfully")
        return redirect(reverse_lazy("memberships:home"))