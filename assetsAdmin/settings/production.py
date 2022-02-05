import dj_database_url


DEBUG = True

SECRET_KEY = 'django-insecure-0g49mcmm=9#bs$u%&o4_r8&np)4-_4s#c@k)1c6sg@o73f+*v!'

# Alterar para o IP do ambiente de produção quando houver.
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config()
}
