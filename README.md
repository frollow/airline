Airline

To use database:

    python manage.py syncdb
    python manage.py migrate cities_light 0001
    python manage.py migrate cities_light 0002
    python manage.py migrate cities_light 0003
    python manage.py migrate cities_light --fake 0003
    python manage.py migrate cities_light
    python manage.py migrate
    python manage.py cities_light --force-all
