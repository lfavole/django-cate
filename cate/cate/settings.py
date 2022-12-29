"""
Django settings for cate project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import sys
from pathlib import Path
from filer.utils.files import get_valid_filename

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(BASE_DIR.parent / "scripts"))
from common import PYTHONANYWHERE, PYTHONANYWHERE_SITE, USERNAME, App

settings = App(BASE_DIR.name).settings

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = settings.SECRET_KEY or "+jt!%+%erdp^y7h37v#68x31+u9ut6^8zryj@#zmu5p$_!u2)u"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = settings.DEBUG

if not DEBUG:
	CSRF_COOKIE_SECURE = True
	SESSION_COOKIE_SECURE = True
	CONN_MAX_AGE = 600
	ALLOWED_HOSTS = [settings.HOST]
else:
	ALLOWED_HOSTS = ["localhost", "127.0.0.1", "192.168.43.206"]

# Application definition

INSTALLED_APPS = [
	"django.contrib.admin",
	"django.contrib.admindocs",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"adminsortable2",
	"easy_thumbnails",
	"filer",
	"mptt",
	"cate",
	"uservisit",
	"espacecate",
	# "aumonerie",
	"calendrier_avent_2022",
]

MIDDLEWARE = [
	"django.middleware.security.SecurityMiddleware",
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.common.CommonMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
	"uservisit.middleware.UserVisitMiddleware",
]

ROOT_URLCONF = "cate.urls"

TEMPLATES = [
	{
		"BACKEND": "django.template.backends.django.DjangoTemplates",
		"DIRS": [],
		"APP_DIRS": True,
		"OPTIONS": {
			"context_processors": [
				"django.template.context_processors.debug",
				"django.template.context_processors.request",
				"django.contrib.auth.context_processors.auth",
				"django.contrib.messages.context_processors.messages",
				"cate.context_processors.app_name",
				"espacecate.context_processors.navbar_processor",
			],
		},
	},
]

WSGI_APPLICATION = "cate.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": BASE_DIR / "db.sqlite3",
	}
} if settings.USE_SQLITE else {
	"default": {
		"ENGINE": "django.db.backends.mysql",
		"NAME": settings.DB_NAME,
		"USER": settings.DB_USER,
		"PASSWORD": settings.DB_PASSWORD,
		"HOST": (USERNAME + ".mysql." + PYTHONANYWHERE_SITE.replace("pythonanywhere.com", "pythonanywhere-services.com")) if PYTHONANYWHERE else settings.DB_HOST,
		"OPTIONS": {
			"init_command": "SET sql_mode=\"STRICT_TRANS_TABLES\"",
		},
	}
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "fr-FR"

TIME_ZONE = "Europe/Paris"

USE_I18N = True
USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "src/"]
STATIC_ROOT = BASE_DIR / "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"

PRIVATE_MEDIA_URL = "private/"
PRIVATE_MEDIA_ROOT = BASE_DIR / "private/"

FILER_STORAGES = {
	"public": {
		"main": {
			"ENGINE": "filer.storage.PublicFileSystemStorage",
			"OPTIONS": {
				"location": MEDIA_ROOT,
				"base_url": MEDIA_URL,
			},
			"UPLOAD_TO": "cate.settings.generate_filename",
			"UPLOAD_TO_PREFIX": "",
		},
		"thumbnails": {
			"ENGINE": "filer.storage.PublicFileSystemStorage",
			"OPTIONS": {
				"location": MEDIA_ROOT,
				"base_url": MEDIA_URL,
			},
			"THUMBNAIL_OPTIONS": {
				"base_dir": "thumbs",
			},
		},
	},
	"private": {
		"main": {
			"ENGINE": "filer.storage.PrivateFileSystemStorage",
			"OPTIONS": {
				"location": PRIVATE_MEDIA_ROOT,
				"base_url": PRIVATE_MEDIA_URL,
			},
			"UPLOAD_TO": "cate.settings.generate_filename",
			"UPLOAD_TO_PREFIX": "",
		},
		"thumbnails": {
			"ENGINE": "filer.storage.PrivateFileSystemStorage",
			"OPTIONS": {
				"location": PRIVATE_MEDIA_ROOT,
				"base_url": PRIVATE_MEDIA_URL,
			},
			"THUMBNAIL_OPTIONS": {
				"base_dir": "thumbs",
			},
		},
	},
}

FILER_ENABLE_PERMISSIONS = True

def generate_filename(_instance, filename: str):
	ret = get_valid_filename(filename).replace("_", "-")
	while "--" in ret:
		ret = ret.replace("--", "-")
	return ret

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
