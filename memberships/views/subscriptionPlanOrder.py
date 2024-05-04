from memberships.models import SubscriptionPlan, MembershipPlans, Pricing
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from datetime import timedelta, datetime



@method_decorator(login_required, name='dispatch')
class SubscriptionPlanOrder(CreateView):
    model = SubscriptionPlan
    fields = ["membership_plan", "user", "pricing"]
    
    
    def post(self, request: HttpRequest, membershipPlanSlug: str, packageSlug: str) -> HttpResponse:
        try:
            membershipPlan = MembershipPlans.objects.get(slug=membershipPlanSlug)
            package = Pricing.objects.get(slug=packageSlug)
            date_str = request.POST.get("booking_date")
            number_of_people = request.POST.get("number_of_people")
            date_format = "%m/%d/%Y"
            start_date = datetime.strptime(date_str, date_format)
            end_date = start_date + timedelta(days=package.days)
            SubscriptionPlan.objects.create(
                membership_plan=membershipPlan,
                user=request.user,
                pricing=package,
                number_of_people = number_of_people,
                start_date = start_date,
                end_date = end_date
                
            )
            messages.success(request, "Subscription Plan created successfully")
        except MembershipPlans.DoesNotExist:
            messages.error(request, "Membership plan not found.")
        except Pricing.DoesNotExist:
            messages.error(request, "Pricing package not found.")
        
        return redirect(reverse_lazy("memberships:home"))