from django.contrib import admin
from assets.models.models_assets import Assetstable

class AssetstableAdmin(admin.ModelAdmin):
    list_display = ('coin', 'user_id', 'timer')
    raw_id_fields = ('user_id',)
    # filter_horizontal = ('user_id',)



admin.site.register(Assetstable, AssetstableAdmin)
