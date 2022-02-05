from django.views.generic import ListView
from assets.models.models_assets import Assetstable
from django.contrib.auth.mixins import LoginRequiredMixin


class ListcoinsView(LoginRequiredMixin, ListView):
    template_name = 'listcoins/listcoins.html'
    model = Assetstable

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coins'] = Assetstable.objects.filter(user_id=self.request.user)
        return context
