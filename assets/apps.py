from django.apps import AppConfig


class AssetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assets'
    verbose_name = "Gerenciamento de Ativos"

    def ready(self):
        from assets.datascheduler import updatedata
        updatedata.start()
