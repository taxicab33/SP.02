from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from accounts.forms import RegisterUserForm, LoginUserForm
from accounts.models import User


class UserLoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Вход в систему"
        return context

    def get_success_url(self):
        return reverse_lazy('equipment')


class UserRegistrationView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('equipment')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация в системе"
        return context


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


class UserListView(ListView):
    model = User
    template_name = 'accounts/users_list.html'
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Пользователи системы"
        return context
