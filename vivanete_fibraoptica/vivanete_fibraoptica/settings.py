"""
Django settings for vivanete_fibraoptica project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from django.contrib.messages import constants as messages

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clientes',
    'servicos',
    'pagamentos',
    'contato',
    'sobre',
    'django_recaptcha',
    'django_distill',
    # 'django_otp',
    # 'django_otp.plugins.otp_static',   # Para códigos estáticos
    # 'django_otp.plugins.otp_totp',     # Para aplicativos autenticadores (Google Authenticator)
    # 'two_factor',
    # 'phonenumber_field',  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django_otp.middleware.OTPMiddleware',
    'vivanete_fibraoptica.middleware.AdminIPRestrictionMiddleware',
]

ROOT_URLCONF = 'vivanete_fibraoptica.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'vivanete_fibraoptica.wsgi.application'
WSGI_APPLICATION = 'vivanete_fibraoptica.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vivanete_app',
        'USER': 'vivanete_app_owner',
        'PASSWORD': 'SInEa5T0WuKq',
        'HOST': 'ep-old-mode-a522n2ad.us-east-2.aws.neon.tech',
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Diretório onde os arquivos estáticos serão coletados (usado em produção)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Diretórios onde o Django procurará por arquivos estáticos adicionais
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

GERENCIANET_CLIENT_ID = os.getenv('GERENCIANET_CLIENT_ID')
GERENCIANET_CLIENT_SECRET = os.getenv('GERENCIANET_CLIENT_SECRET')
GERENCIANET_CERTIFICADO = os.getenv('GERENCIANET_CERTIFICADO')
GERENCIANET_CHAVE_PIX = os.getenv('GERENCIANET_CHAVE_PIX')
GERENCIANET_AMBIENTE = os.getenv('GERENCIANET_AMBIENTE', 'sandbox')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CONTACT_EMAIL = 'mdkjo23@gmail.com'

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

AUTHORIZED_IPS = [
    '127.0.0.1',  # IP local
    #'192.168.100.1',   Substitua pelo seu IP público
    # Adicione outros IPs autorizados
]

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False

# LOGIN_URL = 'two_factor:login'
# LOGIN_REDIRECT_URL = 'home'  # Substitua 'home' pela URL que você deseja redirecionar após o login
# LOGOUT_REDIRECT_URL = 'home'

# settings.py

# Configurações de reCAPTCHA
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_USE_SSL = True
RECAPTCHA_REQUIRED_SCORE = 0.5 # for v3 captcha