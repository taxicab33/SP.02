from django.urls import path, include

from accounts.views import *

urlpatterns = [
    path('inventory', UserRegistrationView.as_view(), name='inventory'),
]
