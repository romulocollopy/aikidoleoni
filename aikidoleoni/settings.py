"""
Django settings for aikidoleoni project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys
from pathlib import Path
from decouple import config, Csv
from dj_database_url import parse as db_url

PROJECT_DIR = Path(__file__).parents[1]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default='*')

ADMINS = (
    ('Rômulo Collopy', 'romulocollopy@gmail.com'),
    )

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pipeline',
    'ckeditor',
    'aikidoleoni.core',
    'aikidoleoni.blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'aikidoleoni.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.core.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'aikidoleoni.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///'+ str(PROJECT_DIR / 'db.sqlite3'),
        cast=db_url
    )
}

STATICFILES_DIRS = (
  str(PROJECT_DIR /'bower_components'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

STATICFILES_FINDERS = (
    'pipeline.finders.FileSystemFinder',
    'pipeline.finders.AppDirectoriesFinder',
    'pipeline.finders.CachedFileFinder',
    'pipeline.finders.PipelineFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

PIPELINE_CSS = {
    'libraries': {
        'source_filenames': (
            'bootstrap/dist/css/bootstrap.css',
            'core/css/clean_blog.css',
            'core/css/styles.less',
        ),
        'output_filename': 'css/libraries.min.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'libraries': {
        'source_filenames': (
            'jquery/dist/jquery.js',
            'bootstrap/dist/js/bootstrap.js',
            'core/js/clean_blog.js'
        ),
        'output_filename': 'js/libraries.min.js',
    }
}

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = config('STATIC_URL', default='/static/')
STATIC_ROOT = config('STATIC_ROOT', default=str(PROJECT_DIR.parent / 'static'))
MEDIA_URL = config('MEDIA_URL', default='/media/')
MEDIA_ROOT = config('MEDIA_ROOT', default=str(PROJECT_DIR.parent / 'media'))


class DisableMigrations:

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return 'notmigrations'


if 'test' in sys.argv:
    CACHE_MIDDLEWARE_SECONDS = 0
    MIGRATION_MODULES = DisableMigrations()


def gen_html():
    return (
        """<h1>WOW</h1>
        <p>Look here, thas a Rich HTML content</p>
        <p>Bye, now.</p>"""
        )

MOMMY_CUSTOM_FIELDS_GEN = {
    'ckeditor.fields.RichTextField': gen_html,
    }

CKEDITOR_UPLOAD_PATH = "uploads/"

EMAIL_HOST=config('EMAIL_HOST', default='localhost')
EMAIL_PORT=config('EMAIL_PORT', default=45, cast=int)
EMAIL_HOST_USER=config('EMAIL_HOST_USER', default='root')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD', default='root')
EMAIL_USE_SSL=config('EMAIL_USE_SSL', default=False, cast=bool)

