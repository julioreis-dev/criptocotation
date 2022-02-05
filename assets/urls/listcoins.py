from django.urls import path
from assets.views.listcoins import ListcoinsView

app_name = 'list'

urlpatterns = [
    path('alerts/', ListcoinsView.as_view(), name='coins'),
]
