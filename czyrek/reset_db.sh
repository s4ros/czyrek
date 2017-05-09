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

s = Subjects(name='Matematyka', shortcut='MAT', wage=75, is_available=True)
s.save()
s = Subjects(name='J. Polski', shortcut='POL', wage=50, is_available=True)
s.save()
s = Subjects(name='Fizyka', shortcut='FIZ', wage=85, is_available=True)
s.save()
s = Subjects(name='Geografia', shortcut='GEO', wage=60, is_available=True)
s.save()
s = Subjects(name='Biologia', shortcut='BIOL', wage=70, is_available=True)
s.save()

l = Languages(name='Angielski (początkujący)', shortcut='EN-P', level='P' ,is_available=True)
l.save()
l = Languages(name='Angielski (zaawansowany)', shortcut='EN-Z', level='Z' ,is_available=True)
l.save()
l = Languages(name='Rosyjski (początkujący)', shortcut='RU-P', level='P', is_available=True)
l.save()
l = Languages(name='Rosyjski (zaawansowany)', shortcut='RU-Z', level='Z', is_available=True)
l.save()
l = Languages(name='Niemiecki (początkujący)', shortcut='DE-P', level='P', is_available=True)
l.save()
l = Languages(name='Niemiecki (zaawansowany)', shortcut='DE-Z', level='Z', is_available=True)
l.save()

s = Schools(name=u'Liceum Ogolnoksztalcace', shortcut='LO', is_available=True)
s.save()
s = Schools(name=u'Technikum', shortcut='TE', is_available=True)
s.save()
s = Schools(name=u'Szkola Zawodowa', shortcut='ZA', is_available=True)
s.save()

school_id=Schools.objects.get(pk=1)
p = Profiles(name='Humanistyczny', school_id=school_id, shortcut="HUM-{}".format(school_id.shortcut), is_available=True)
p.save()
school_id=Schools.objects.get(pk=2)
p = Profiles(name='Informatyczny', school_id=school_id, shortcut="INF-{}".format(school_id.shortcut), is_available=True)
p.save()
school_id=Schools.objects.get(pk=1)
p = Profiles(name='Matematyczno Fizyczny', school_id=school_id, shortcut="MFIZ-{}".format(school_id.shortcut), is_available=True)
p.save()
school_id=Schools.objects.get(pk=3)
p = Profiles(name='Mechaniczny', school_id=school_id, shortcut="MECH-{}".format(school_id.shortcut), is_available=True)
p.save()
school_id=Schools.objects.get(pk=2)
p = Profiles(name='Ekonomiczny', school_id=school_id, shortcut="EKO-{}".format(school_id.shortcut), is_available=True)

_EOF

if [[ "$1" == "run" ]]; then
  python manage.py runserver 0.0.0.0:8000
fi
