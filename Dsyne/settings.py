# The above code is for the django admin customizer.
"""
Django settings for Dsyne project.

Generated by 'django-admin startproject' using Django 3.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import dj_database_url
import os
from pathlib import Path
from decouple import config
# import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# create a file called `.env` in the root directory of the project
# generate a secret key with:python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' from this:
# https://www.codingforentrepreneurs.com/blog/create-a-one-off-django-secret-key/
SECRET_KEY = config(
    "SECRET_KEY", 'django-insecure-z-*l#b#9_0gvk*t4o+3n*d71*v6-ce6r97za!@&wfnz&p6p#60')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost")


# Application definition

INSTALLED_APPS = [
    "jazzmin",

    # django-admin style for django_cms
    "djangocms_admin_style",
    'djangocms_text_ckeditor',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    # third party app
    "rest_framework",
    "ckeditor",
    "cloudinary",
    # internal app
    "blog",

    # main app
    "account",
    # for django filer
    "filer",
    "easy_thumbnails",
    "mptt",
    # micelleneous plugins
    "djangocms_link",
    "djangocms_file",
    "djangocms_picture",
    "djangocms_video",
    "djangocms_googlemap",
    "djangocms_snippet",
    "djangocms_style",
    # django_cms thirdparty apps
    "django.contrib.sites",
    "cms",
    "menus",
    "treebeard",
    "sekizai",
    "translations",
    'tinymce',
    "portfolio",
    "whitenoise.runserver_nostatic",

]

MIDDLEWARE = [
    # middleware for django_cms
    "cms.middleware.utils.ApphookReloadMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # middleware for django_cms
    "django.middleware.locale.LocaleMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = "Dsyne.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates_account"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                # django_cms templates context processors
                "cms.context_processors.cms_settings",
                "django.template.context_processors.i18n",
                "sekizai.context_processors.sekizai",
            ],
        },
    },
]

# templates config for django_cms
CMS_TEMPLATES = [
    ("base.html", "Empty template"),
    ("portfolio/index.html", "portfolio template"),
]

WSGI_APPLICATION = "Dsyne.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# DATABASES = {}

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'dsyne',
            'USER': config('POSTGRES_USER'),
            'PASSWORD': config("POSTGRES_PASSWORD"),
            'HOST': config("POSTGRES_HOST"),
            'PORT': config("POSTGRES_PORT"),
            'OPTIONS': {
                'sslmode': 'require'
            }
        }
    }


# POSTGRES_DB = config("POSTGRES_DB")
# POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
# POSTGRES_USER = config("POSTGRES_USER")
# POSTGRES_HOST = config("POSTGRES_HOST")
# POSTGRES_PORT = config("POSTGRES_PORT")

# POSTGRES_READY = (
#     POSTGRES_DB is not None
#     and POSTGRES_PASSWORD is not None
#     and POSTGRES_USER is not None
#     and POSTGRES_HOST is not None
#     and POSTGRES_PORT is not None
# )

# if POSTGRES_READY:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.postgresql",
#             "NAME": POSTGRES_DB,
#             "USER": POSTGRES_USER,
#             "PASSWORD": POSTGRES_PASSWORD,
#             "HOST": POSTGRES_HOST,
#             "PORT": POSTGRES_PORT,
#         }
#     }


db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# setting a site ID for django_cms

SITE_ID = 1

X_FRAME_OPTIONS = "SAMEORIGIN"

USE_I18N = True
USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = BASE_DIR / 'staticfiles'
# add the directory of your static files here.
# Make sure the name are different from those of other static files


# media urls for django_cms
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# for thumbnail filer
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


""" This settings is for the django admin customizer """

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Dsyne Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Dsyne",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Dsyne",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "../static/media/images/dsyne 2 LOGO 1.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the Dsyne CMS"
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": "darkly",
}

# CKEDITOR_SETTINGS = {
#     'language': '{{ language }}',
#     'toolbar': 'CMS',
#     'skin': 'moono',
# }
