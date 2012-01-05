import os
gettext = lambda s: s

from site_settings import *

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Europe/Moscow'

# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"

# Additional locations of static files
STATICFILES_DIRS = (
    #os.path.join(PROJECT_PATH, 'static'),
)

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    #'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'zinnia.context_processors.version'
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'loginza.authentication.LoginzaBackend',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
)

LANGUAGES = [
    #('en', gettext('English')),
    ('ru', gettext('Russian')),
]

CMS_PERMISSION = True

CMS_SEO_FIELDS = True

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',

    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.text',
    'cms.plugins.twitter',

    'filer',
    #'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    #'cmsplugin_filer_image', # doesn't work
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    'reversion',
    #'cms_search',

    'loginza',
    'users',

    'tagging',
    'zinnia',
    'zinnia.plugins',
)

# TODO: configure logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Loginza settings
LOGINZA_DEFAULT_PROVIDERS_SET = 'google,vkontakte,facebook,livejournal,yandex,mailru,twitter,rambler,odnoklassniki'
#google, yandex, mailruapi, mailru, vkontakte, facebook, twitter, loginza, myopenid, webmoney, rambler, flickr, lastfm, verisign, aol, steam, openid.

# !!!! can't use reverse url resolver here (raises ImportError), so we should carefully control paths
LOGINZA_AMNESIA_PATHS = ('/users/complete_registration/',)

#ZINNIA_ENTRY_BASE_MODEL = 'zinnia.plugins.placeholder.EntryPlaceholder'
