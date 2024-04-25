from django.urls import path
from .views.sign_in import SignInView
from .views.sign_up import SignUpView


app_name = "users"


urlpatterns = [
    path("sign_in/", SignInView.as_view(), name="sign_in"),
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
]