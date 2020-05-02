django version check
    python -m django --version

django subcommands check
    django-admin

install inital project setting
    pip install Django
    django-admin startproject [project name]
    python manage.py startapp [application name]

run django
    python manage.py runserver

move admin site
    http://127.0.0.1:8000/admin/
    on command

templates
    blog -> templates -> blog -> index.html....
    add html -> settings.py -> add blog.apps.BlogConfig at installed_app
    base.html : parents template
                the others templates inherit from base.html



