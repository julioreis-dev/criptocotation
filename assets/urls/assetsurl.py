from django.urls import path
from assets.views.views import IndexTemplateView

app_name = 'home'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
]
