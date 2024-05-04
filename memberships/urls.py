from django.urls import path
from .views.home import HomeView, PlanDetailView, PackageView
from .views.subscriptionPlanView import SubscriptionPlanView
from .views.subscriptionPlanOrder import SubscriptionPlanOrder
from .views.orderListView import OrderListView

app_name = "memberships"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("package/", PackageView.as_view(), name="packageView"),
    path("plans/<slug:slug>/", PlanDetailView.as_view(), name="plan_detail"),
    path("subscription/<slug:membershipPlanSlug>/<slug:packageSlug>/", SubscriptionPlanView.as_view(), name="subscription"),
    path("subscription/order/<slug:membershipPlanSlug>/<slug:packageSlug>/", SubscriptionPlanOrder.as_view(), name="subscription_order"),
    path("orders/", OrderListView.as_view(), name="order_list"),
]
