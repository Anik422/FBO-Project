
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("memberships.urls")),
    path("accounts/", include("users.urls")),
    # path("accounts/reset_password/", PasswordResetView.as_view(), name="password_reset"),   
    # path("accounts/reset_password_confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path("accounts/reset_password_done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path("accounts/reset_password_complete/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
