# -*- coding: utf-8 -*-
from server.settings.components import config
# Caching
# https://docs.djangoproject.com/en/2.2/topics/cache/

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('REDIS_LOC'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        },
        'KEY_PREFIX': 'morattendance'
    },
    'axes_cache': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}


# django-axes
# https://django-axes.readthedocs.io/en/latest/configuration.html
# See #known-configuration-problems section

AXES_CACHE = 'axes_cache'
