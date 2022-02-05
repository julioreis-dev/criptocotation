from django.urls import path
from assets.views.deletealert import DeleteAlertView

app_name = 'delete'

urlpatterns = [
    path('alert/<pk>', DeleteAlertView.as_view(), name='alert'),
]