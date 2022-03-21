from assetsAdmin.settings.settings import *
import dj_database_url


SECRET_KEY = config('SECRET_KEY', cast=str)

DEBUG = False

# Alterar para o IP do ambiente de produção quando houver.
ALLOWED_HOSTS = ['criptocoincotation.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}
