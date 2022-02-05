from django.urls import path
from assets.views.updatealert import AlertUpdateView

app_name = 'update'

urlpatterns = [
    path('alert/<pk>', AlertUpdateView.as_view(), name='alert'),
]
