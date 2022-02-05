from django.urls import reverse_lazy
from django.views.generic import UpdateView
from assets.models.models_assets import Assetstable
from django.contrib.auth.mixins import LoginRequiredMixin


class AlertUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "updatealert/updatealert.html"
    model = Assetstable
    fields = ['nameconfig', 'coin', 'sell', 'buy', 'timer']
    context_object_name = 'coin'
    success_url = reverse_lazy("list:coins")

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['info'] = salutation()
    #     return context
