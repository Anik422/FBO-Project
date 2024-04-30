from django.urls import path
from .views.home import HomeView, PlanDetailView, PlansView

app_name = "memberships"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("plans/", PlansView.as_view(), name="plans"),
    path("plans/<slug:slug>/", PlanDetailView.as_view(), name="plan_detail"),
]
