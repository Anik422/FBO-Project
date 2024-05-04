from memberships.models import SubscriptionPlan, MembershipPlans, Pricing
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from datetime import timedelta, datetime


class OrderListView(ListView):
    model = SubscriptionPlan
    template_name = "memberships/order_list.html"
    context_object_name = "orders"

    @method_decorator(login_required)
    def get(self, request: HttpRequest) -> HttpResponse:
        orders = SubscriptionPlan.objects.filter(user=request.user).order_by("-id")
        return render(request, self.template_name, {self.context_object_name: orders})
