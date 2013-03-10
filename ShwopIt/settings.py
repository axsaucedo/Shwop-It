# Django settings for ShwopIt project.

##################### IMPORTANT!!!! #######################
#If this is run in the server the following points should be modified:
#MEDIA_ROOT = '/home/bitnami/apps/django/django_projects/AffiLinkProject/AffiLinkProject/media/'
#STATIC_ROOT = '/home/bitnami/apps/django/django_projects/AffiLinkProject/AffiLinkProject/static/'
#TEMPLATE_DIRS = ('/home/bitnami/apps/django/django_projects/AffiLinkProject/AffiLinkProject/templates',)

DEBUG = True
TEMPLATE_DEBUG = DEBUG


#USERENA OVERRIDE SETTINGS
USERENA_REDIRECT_ON_SIGNOUT = '/'
USERENA_SIGNIN_REDIRECT_URL = '/'
USERENA_SIGNIN_AFTER_SIGNUP = False
USERENA_ACTIVATION_DAYS = 30
USERENA_ACTIVATION_NOTIFY = True
USERENA_ACTIVATION_REQUIRED = False

ADMINS = (
    ('admin', 'axsauze@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'shwopitdb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '5664021a',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# If run in the server it should be changed to:
# MEDIA_ROOT = '/home/bitnami/apps/django/django_projects/ShwopItProject/ShwopIt/media/'
MEDIA_ROOT = '/Users/axsauze/IdeaProjects/ShwopItProject/ShwopIt/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/adminmedia/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# If run in server it should be changed to:
# STATIC_ROOT = '/home/bitnami/apps/django/django_projects/ShwopItProject/ShwopIt/static/'
STATIC_ROOT = '/Users/axsauze/IdeaProjects/ShwopItProject/ShwopIt/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '29j%o-voipvb76f-b_jrqg@9cks^#!3mj9)bd-0d4w1)&c0(qw'

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
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ShwopIt.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ShwopIt.wsgi.application'

#TEMPLATE_DIRS = ('/home/bitnami/apps/django/django_projects/ShwopItProject/templates')
TEMPLATE_DIRS = ('/Users/axsauze/IdeaProjects/ShwopItProject/templates',)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'userena',
    'guardian',
    'easy_thumbnails',
    'accounts',
    'Shwopper',
)

#USED FOR USERENA AND GUARDIAN
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

ANONYMOUS_USER_ID = -1
#USED FOR USERENA AND GUARDIAN


#OVERRIDING AUTH METHODS
AUTH_PROFILE_MODULE = 'accounts.MyProfile'

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
#OVERRIDING AUTH METHODS

#SETTINGS FOR EMAIL
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hackasoton@gmail.com'
EMAIL_HOST_PASSWORD = '654asdf.'
#SETTINGS FOR EMAIL


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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
