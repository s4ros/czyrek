#!/bin/bash
set -e

. ../bin/activate
rm -f db.sqlite3
rm -rf czyrek/manager/migrations

python manage.py migrate --run-syncdb
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# INSERT INTO auth_suer VALUES (pbkdf2_sha256$30000$bJKBuxUfOj4M$pSjkUjwlI61RVNdULS70CNXTWeIsburK2gRJsDqYJ5s=,2017-03-15 18:07:45.875844,1,,,s4ros@s4ros.it,1,1,2017-03-14 17:55:22.761474,s4ros)
