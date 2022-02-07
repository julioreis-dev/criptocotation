from django.contrib import admin
from assets.models.models_assets import Assetstable, Coincotationtable


class AssetstableAdmin(admin.ModelAdmin):
    list_display = ('coin', 'user_id', 'timer')
    raw_id_fields = ('user_id',)


class CoincotationtableAdmin(admin.ModelAdmin):
    list_display = ('description', 'price')


admin.site.register(Assetstable, AssetstableAdmin)
admin.site.register(Coincotationtable, CoincotationtableAdmin)
