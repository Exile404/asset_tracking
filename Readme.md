# Setup the Project
pip install -r requirements.txt

# Database Configuration

Change in settings.py

DATABASES = {\
    'default': {\
        'ENGINE': 'django.db.backends.postgresql',\
        'NAME': 'asset_tracking', #Replace with your database name\
        'USER': 'postgres', #Default user for postgresql\
        'PASSWORD': '1234',# Replace with your postgresql server\
        'HOST': 'localhost',\
        'PORT': '5432',\
    }\
}

# Get API Documention
run => python manage.py runserver
Visit: http://localhost:8000/swagger/

# Test all API together

run => py manage.py test
