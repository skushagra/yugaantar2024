from django.urls import path
from .views import RegisterEarlyUserView

urlpatterns = [
    path('register/', RegisterEarlyUserView.as_view(), name='register_early_user'),
]
