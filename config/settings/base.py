"""
Django settings for evolvemedicus project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys
from email.utils import parseaddr
from django.conf.locale.en import formats as en_formats

import environ
from django.utils.translation import ugettext_lazy as _


en_formats.DATE_FORMAT = 'd-m-y'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = environ.Path(__file__) - 3
#print(BASE_DIR)
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))
_ENV = env.str("DJANGO_SETTINGS_MODULE", "config.settings.base")
#FIREBASE_CRED = env("FIREBASE_SCRED")
#creed = os.path.join(BASE_DIR, FIREBASE_CRED)

# PROJECT_DIR = os.path.join(BASE_DIR, os.pardir)
#
# TENANT_APPS_DIR = os.path.join(PROJECT_DIR, os.pardir)
# sys.path.insert(0, TENANT_APPS_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO_SECRET_KEY", default="!!!SET DJANGO_SECRET_KEY!!!",)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "modeltranslation",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_filters",
    "guardian",
    "django_extensions",
    "import_export",
    "evolvemedicus.profiles.apps.ProfilesConfig",
    "evolvemedicus.core.apps.CoreConfig",

]

ACCOUNT_DEFAULT_HTTP_PROTOCOL ="https"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'user_language_middleware.UserLanguageMiddleware',
    # Custom Middlewares
    # 'evolvemedicus.config.middleware.OnlineNowMiddleware',


]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "evolvemedicus/templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",


            ],

        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

#to handle error too many redirect
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]




LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [str(BASE_DIR("evolvemedicus/static"))]
STATIC_ROOT = str(BASE_DIR("static"))

MEDIA_URL = "/media/"
MEDIA_ROOT = str(BASE_DIR("media"))

# Project adjustments
AUTH_USER_MODEL = "profiles.User"
admins_data = env.tuple(
    "DJANGO_ADMINS", default="Open Course <syndicma2020@gmail.com>"
)
ADMINS = tuple(parseaddr(email) for email in admins_data)

# Third-party syndicma settings
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
    "guardian.backends.ObjectPermissionBackend",
)
SITE_ID = 1
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_FORMS = {"signup": "evolvemedicus.profiles.forms.ProfileCreateForm"}
LOGIN_REDIRECT_URL = "profiles:dispatch_login"

ACCOUNT_LOGOUT_REDIRECT_URL = "account_login"

LOGIN_URL = "account_login"
#LOGIN_URLS = '/accounts/login/'

LOGIN_EXEMPT_URLS = (
    r'^admin/$',
    r'^accounts/logout/$',
    r'^accounts/login/$',
    r'^accounts/signup/$',
    r'^accounts/password/change/$',
    r'^accounts/password/set/$',
    r'^accounts/password/reset/done/$',
    r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
    r'^accounts/password/reset/key/done/$',
    r'^accounts/password/reset/$',
)

# trial period
TRIALPERIOD = 90

GUARDIAN_RENDER_403 = True
GUARDIAN_TEMPLATE_403 = "403.html"
GUARDIAN_MONKEY_PATCH = False

# Security settings
CSRF_COOKIE_HTTPONLY = True
# ADMIN_URL = "admin/"

# Delete on production
ACCOUNT_LOGOUT_ON_GET = True

CRONJOBS = [
    ('*/1 * * * *', 'evolvemedicus.core.cron.scheduled_job')
]

COMMENTS_APP = 'django_comments_xtd'

#  To help obfuscating comments before they are sent for confirmation.
COMMENTS_XTD_SALT = (b"Timendi causa est nescire. "
                     b"Aequam memento rebus in arduis servare mentem.")
COMMENTS_XTD_MAX_THREAD_LEVEL = 1
COMMENTS_XTD_CONFIRM_EMAIL = True
COMMENTS_XTD_LIST_ORDER = ('-thread_id', 'order')  # default is ('thread_id', 'order')

# Source mail address used for notifications.
COMMENTS_XTD_FROM_EMAIL = "syndicma2020@gmail.com"

# Contact mail address to show in messages.
COMMENTS_XTD_CONTACT_EMAIL = "syndicma2020@gmail.com"

COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'core.post': {
        'allow_flagging': True,
        'allow_feedback': True,
        'show_feedback': True,
    }
}

SHOW_PUBLIC_IF_NO_TENANT_FOUND = True

# Image resize config
DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_QUALITY = 100
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True

