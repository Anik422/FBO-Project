from django.urls import path
from .views.home import HomeView, PlanDetailView, PackageView
from .views.subscriptionPlanView import SubscriptionPlanView

app_name = "memberships"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("package/", PackageView.as_view(), name="packageView"),
    path("plans/<slug:slug>/", PlanDetailView.as_view(), name="plan_detail"),
    path("subscription/<slug:membershipPlanSlug>/<slug:packageSlug>/", SubscriptionPlanView.as_view(), name="subscription"),
]
