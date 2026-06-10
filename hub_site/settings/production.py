from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['the-english-hub.onrender.com', 'localhost', '127.0.0.1']

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = BASE_DIR / "static_compiled"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

try:
    from .local import *
except ImportError:
    pass