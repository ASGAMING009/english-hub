from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = ['the-english-hub.onrender.com', 'localhost', '127.0.0.1']

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = BASE_DIR / "static_compiled"

try:
    from .local import *
except ImportError:
    pass