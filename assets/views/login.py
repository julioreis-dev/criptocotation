from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from assets.forms.login import LoginForm


class LoginView(View):
    def get(self, request):
        data = {'form': LoginForm()}
        return render(request, 'login/login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if username and password and user:
                login(request, user)
                return HttpResponseRedirect(reverse('list:coins'))

        data = {
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }
        return render(request, 'login/login.html', data)


class LogoutView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home:index'))
