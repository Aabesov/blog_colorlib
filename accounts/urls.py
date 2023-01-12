from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path("register/", views.RegisterUserAPIView.as_view()),
    path("activate/<str:activation_code>/",
         views.ActivateAccountView.as_view(), name="activate_account"),
    path("users/", views.AllUsersAPIView.as_view()),
    # path("login/", views.UserTokenLoginAPIView.as_view()),
    path("login/", views.UserJWTLoginAPIView.as_view()),
    path("logout/", views.UserTokenLogoutAPIView.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]