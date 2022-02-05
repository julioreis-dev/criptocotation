from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, View
from assets.models.models_assets import Assetstable
from django.contrib.auth.mixins import LoginRequiredMixin


# class DeleteAlertView(LoginRequiredMixin, DeleteView):
#     template_name = 'deletealert/deletealert.html'
#     context_object_name = 'alert'
#     model = Assetstable
#     success_url = reverse_lazy('list:coins')

# def DeleteAlertView(request, pk):
#     clientReport = Assetstable.objects.filter(id=int(pk))
#     clientReport.delete()
#     return HttpResponseRedirect(reverse('list:coins'))


class DeleteAlertView(LoginRequiredMixin, View):
    def post(self, request, pk):
        client = self.kwargs['pk']
        clientReport = Assetstable.objects.filter(id=client)
        clientReport.delete()
        return HttpResponseRedirect(reverse('list:coins'))

    # def get_object(self, queryset=None):
    #     if queryset is None:
    #         queryset = self.get_queryset()
    #     client = self.kwargs['pk']
    #     queryset = Assetstable.objects.filter(id=client)
    #
    #     if not queryset:
    #         raise Http404
    #
    # def delete(self, request, *args, **kwargs):
    #     client = self.kwargs['pk']
    #     clientReport = Assetstable.objects.filter(id=client)
    #     clientReport.delete()
    #
    #     return HttpResponseRedirect(reverse('list:coins'))
