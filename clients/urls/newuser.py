from django.urls import path
from clients.views.newuser import NewuserView

app_name = 'newuser'

urlpatterns = [
    path('', NewuserView.as_view(), name='newuser'),
]
