from django.urls import path
from assets.views.registercoin import RegistercoinView

app_name = 'register'

urlpatterns = [
    path('alert/', RegistercoinView.as_view(), name='coin'),
]
