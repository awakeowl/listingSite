from django.urls import path

from accounts.views import SignupView, LoginView, ChangePasswordView, ForgotPasswordView

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('password/forgot/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('password/change/', ChangePasswordView.as_view(), name='change_password'),
]
