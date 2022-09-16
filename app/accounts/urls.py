from django.urls import path, include

from accounts.views import *

urlpatterns = [
    path('accounts/signup', UserRegistrationView.as_view(), name='signup'),
    path('accounts/login', UserLoginView.as_view(), name='login'),
    path('accounts/logout', logout_user, name='logout'),
    path('accounts/users', UserListView.as_view(), name='users')
]
