from django.contrib import admin
from clients.models.models_clients import Clientstable


class ClientstableAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email', 'tel')


admin.site.register(Clientstable, ClientstableAdmin)
