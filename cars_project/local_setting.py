# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iz9^hv%)^+enb-k5@&z%%gl6*@b@b57rs2l1i3_f!*wpv@ku)u'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}