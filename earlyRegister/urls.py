from django.urls import path
from .views import RegisterEarlyUserView, ExportEarlyRegisterView

urlpatterns = [
    path('register/', RegisterEarlyUserView.as_view(), name='register_early_user'),
    path('export/', ExportEarlyRegisterView.as_view(), name='export_early_register')
]
