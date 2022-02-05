from django.urls import path
from assets.views.login import LogoutView

app_name = 'logout'

urlpatterns = [
    path('', LogoutView.as_view(), name='index'),
]
