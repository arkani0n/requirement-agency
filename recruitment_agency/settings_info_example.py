import os


DJANGO_SECURITY_KEY= 'django_security_key'
if os.getenv('DB_NAME') and os.getenv('DB_USER') and os.getenv('DB_PASSWORD') and os.getenv('DB_PORT'):

        DB_INFO={
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('DB_NAME') ,
                'USER': os.getenv('DB_USER'),
                'PASSWORD': os.getenv('DB_PASSWORD'),
                'HOST':'localhost',
                'PORT': os.getenv('DB_PORT')
            }
else:
        DB_INFO={
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'recuirment_agency',
                'USER': 'username',
                'PASSWORD': 'password',
                'HOST':'localhost',
                'PORT':'5432'
            }