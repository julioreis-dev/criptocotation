from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from assets.models.models_assets import Assetstable
from assets.forms.assets import AssetsForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistercoinView(LoginRequiredMixin, CreateView):
    template_name = 'coin/registercoin.html'
    model = Assetstable
    form_class = AssetsForm
    login_url = '/login/'
    success_url = reverse_lazy('home:index')

    def post(self, request, *args, **kwargs):
        form = AssetsForm(data=request.POST)

        if form.is_valid():
            nameconfig = form.cleaned_data.get('nameconfig')
            coin = form.cleaned_data.get('coin')
            sell = form.cleaned_data.get('sell')
            buy = form.cleaned_data.get('buy')
            timer = form.cleaned_data.get('timer')

            assets = Assetstable(nameconfig=nameconfig, coin=coin, sell=sell,
                                 buy=buy, timer=timer, user_id=request.user)
            assets.save()
            return HttpResponseRedirect(reverse_lazy('list:coins'))
