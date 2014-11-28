from settings import BASE_DIR
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "avia",
        "USER": "avia",
        "PASSWORD": "12345",
        "HOST": "localhost",
        "PORT": "",
    }
}
