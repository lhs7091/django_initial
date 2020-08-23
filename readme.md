# Django tutorial
    https://docs.djangoproject.com/en/3.1/

# django version check    
    python -m django --version

# django subcommands check
    django-admin

# install inital project setting
    pip install Django
    django-admin startproject [project name]
    python manage.py startapp [application name]

# run django
    python manage.py runserver

# move admin site
    python manage.py createsuperuser
    http://127.0.0.1:8000/admin/
    on command

# templates
    blog -> templates -> blog -> index.html....
    add html -> settings.py -> add blog.apps.BlogConfig at installed_app
    base.html : parents template
                the others templates inherit from base.html

# make a model and migration
    create model class in models.py
    python manage.py makemigrations
    python manage.py sqlmigrate [application name] [migration No.]
    python manage.py migrate

    to check sql command
        python manage.py shell

# User Registration 
    python manage.py startapp users 

    pip install django-crispy-forms -> setting.py
    -> installed_apps -> 'crispy_forms' -> the end line  
    -> add CRISPY_TEMPLATE_PACK = 'bootstrap4'  


