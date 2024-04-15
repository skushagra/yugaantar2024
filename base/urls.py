from django.urls import path
from .views import HomeView, LoginView, EarlyRegisterView

urlpatterns = [
    path("", HomeView.as_view(), name="HomeView"),
    path("login", LoginView.as_view(), name="LoginView"),
    path("early", EarlyRegisterView.as_view(), name="EarlyRegisterView"),
]