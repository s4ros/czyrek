#!/bin/bash
set -e

. ../bin/activate
rm -f db.sqlite3
rm -rf czyrek/manager/migrations

python manage.py migrate --run-syncdb
python manage.py migrate

# add user admin:asdqwe123
echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'asdqwe123')" | python manage.py shell

# dodawanie kilku predefiniowanych przedmiotow
cat << _EOF | python manage.py shell
from czyrek.manager.models import Subjects
from czyrek.manager.models import Schools
from czyrek.manager.models import Languages
from czyrek.manager.models import Profiles

s = Subjects(name='Matematyka', wage=75, is_available=True)
s.save()
s = Subjects(name='J. Polski', wage=50, is_available=True)
s.save()
s = Subjects(name='Fizyka', wage=85, is_available=True)
s.save()
s = Subjects(name='Geografia', wage=60, is_available=True)
s.save()
s = Subjects(name='Biologia', wage=70, is_available=True)
s.save()

l = Languages(name='Angielski', is_available=True)
l.save()
l = Languages(name='Rosyjski', is_available=True)
l.save()
l = Languages(name='Niemiecki', is_available=True)
l.save()

s = Schools(name=u'Liceum Ogolnoksztalcace', is_available=True)
s.save()
s = Schools(name=u'Technikum', is_available=True)
s.save()
s = Schools(name=u'Szkola Zawodowa', is_available=True)
s.save()

p = Profiles(name='Humanistyczny', school_id=Schools.objects.get(pk=1), is_available=True)
p.save()
p = Profiles(name='Informatyczny', school_id=Schools.objects.get(pk=2), is_available=True)
p.save()
p = Profiles(name='Matematyczno Fizyczny', school_id=Schools.objects.get(pk=1), is_available=True)
p.save()
p = Profiles(name='Mechaniczny', school_id=Schools.objects.get(pk=3), is_available=True)
p.save()
p = Profiles(name='Ekonomiczny', school_id=Schools.objects.get(pk=2), is_available=True)

_EOF

python manage.py runserver 0.0.0.0:8000
