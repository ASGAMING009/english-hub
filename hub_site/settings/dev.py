from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-jkz6n=$8dsqq@6kky4*wr-j5oko_t#$yb!ew^e%7w#+=u%vybz"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
# TRUST THE TUNNEL!
CSRF_TRUSTED_ORIGINS = ['https://postconvulsive-dario-actuarially.ngrok-free.dev']