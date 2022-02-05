from django.urls import reverse_lazy
from django.views.generic import CreateView
from assets.views.greet import salutation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from clients.models.models_clients import Clientstable
from clients.forms.newclients import ClientsForm, CreateUserForm



class NewuserView(CreateView):
    template_name = 'newuser/newuser.html'
    # model = User
    form_class = CreateUserForm
    success_url = reverse_lazy('home:index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['info'] = salutation()
    #     return context


# class NewuserView(CreateView):
#     template_name = 'newuser/newuser.html'
#     model = Clientstable
#     form_class = ClientsForm
#     success_url = reverse_lazy('home:index')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['info'] = salutation()
#         return context
