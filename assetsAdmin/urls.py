"""assetsAdmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assets.urls.assetsurl')),
    path('new/', include('assets.urls.registercoin')),
    path('newuser/', include('clients.urls.newuser')),
    path('login/', include('assets.urls.login')),
    path('logout/', include('assets.urls.logout')),
    path('', include('django.contrib.auth.urls')),
    path('list/', include('assets.urls.listcoins')),
    path('update/', include('assets.urls.updatealert')),
    path('delete/', include('assets.urls.deletealert')),
]

admin.AdminSite.site_header = "Criptocoin Admin"
admin.AdminSite.site_title = "Criptocoin"
admin.AdminSite.index_title = "Sistema Administrativo"