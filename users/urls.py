from django.urls import path
from .views.sign_in import SignInView
from .views.sign_up import SignUpView, ActivateView
from .views.sign_out import SignOutView, SignOutConfirmationView
from .views.profile import ProfileView

app_name = "users"

urlpatterns = [
    path("login/", SignInView.as_view(), name="sign_in"),
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name='activate'),
    path("sign_out_confirmation/", SignOutConfirmationView.as_view(), name="sign_out_confirmation"),
    path("sign_out/", SignOutView.as_view(), name="sign_out"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
