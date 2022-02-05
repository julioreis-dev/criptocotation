from django.urls import path
from assets.views.login import LoginView

app_name = 'login'

urlpatterns = [
    path('', LoginView.as_view(), name='index'),
]