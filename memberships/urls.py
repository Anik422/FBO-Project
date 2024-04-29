from django.urls import path
from .views.home import HomeView

app_name = "memberships"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
