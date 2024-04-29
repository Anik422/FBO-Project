from django.urls import path
from .views.sign_in import SignInView
from .views.sign_up import SignUpView, ActivateView
from .views.sign_out import SignOutView, SignOutConfirmationView
from .views.profile import ProfileView
from .views.forgot_password import ForgotPasswordView, ResetPasswordView, ResetPasswordEmailDoneView

app_name = "users"

urlpatterns = [
    path("login/", SignInView.as_view(), name="sign_in"),
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name='activate'),
    path("sign_out_confirmation/", SignOutConfirmationView.as_view(), name="sign_out_confirmation"),
    path("sign_out/", SignOutView.as_view(), name="sign_out"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("forgot_password/", ForgotPasswordView.as_view(), name="forgot_password"),
    path("reset_password/<uidb64>/<token>/", ResetPasswordView.as_view(), name="password_reset"),
    path("reset_password_done/", ResetPasswordEmailDoneView.as_view(), name="password_reset_done"),
]
