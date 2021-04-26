from .base import *

ALLOWED_HOSTS    = ['3.34.248.9']
STATIC_ROOT      = BASE_DIR / 'static/'
STATICFILES_DIRS = []

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'pybo',
        'USER'     : 'dbmasteruser',
        'PASSWORD' : '6)3nx$RKyA_|4M0r4&JEzC3f#C^`E5]4',
        'HOST'     : 'ls-0f5ee97237487fbe946fa5fcefaef594df20e630.cytuafyw4thv.ap-northeast-2.rds.amazonaws.com',
        'PORT'     : '3306',
        'OPTIONS'  : {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}