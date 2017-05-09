# -*- coding: utf-8 -*-
from django import forms

from .models import Candidate, Schools, Languages, Subjects, Profiles
from django.contrib.auth.models import User


################################################
# Formularz dodawania uzytkownikow
class AddUserPostForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Hasło")
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name',
                  'last_name', 'is_staff', 'is_active',)
        labels = {
            'username': 'Nazwa użytkownika',
            # 'password': 'Hasło',
            'email': 'Adres E-Mail',
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'is_staff': 'Uprawnienia administratora',
            'is_active': 'Aktywny?',
        }

################################################
# Formualrz edycji uzytkownika
class EditUserForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput(), label="Hasło")
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'is_staff', 'is_active',)
        labels = {
            'username': 'Nazwa użytkownika',
            # 'password': 'Hasło',
            'email': 'Adres E-Mail',
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'is_staff': 'Uprawnienia administratora',
            'is_active': 'Aktywny?',
        }


################################################
# Formularz logowania - homepage
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Hasło")

    class Meta:
        model = User
        fields = ('username', 'password',)
        labels = {
            'username': 'Nazwa użytkownika',
        }

################################################
# Forularz dodawania Kandydata
class AddCandidatePostForm(forms.ModelForm):
    # TODO: Define other fields here
    class Meta:
        model = Candidate
        photo = forms.FileField(label='Wybierz plik', help_text="Tekst wspomagajacy")
        fields = ('name', 'surname', 'phone', 'pesel',
                  'birthdate', 'last_school',
                  'primary_school', 'secondary_school', 'third_school',
                  'subject_one', 'subject_two', 'subject_three',
                  'primary_language', 'secondary_language',
                  'photo',
                  )
        labels = {
            'name': 'Imiona',
            'surname': 'Nazwisko',
            'phone': 'Telefon kontaktowy',
            'pesel': 'Numer PESEL',
            'birthdate': 'Data urodzenia',
            'last_school': 'Poprzednia szkoła',
            'primary_school': 'Preferowany profil/szkoła #1',
            'secondary_school': 'Preferowany profil/szkoła #2',
            'third_school': 'Preferowany profil/szkoła #3',
            'primary_language': 'Preferowany język obcy',
            'secondary_language': 'Alternatywny język obcy',
            'subject_one': 'Przedmiot do punktacji #1',
            'subject_two': 'Przedmiot do punktacji #2',
            'subject_three': 'Przedmiot do punktacji #3',
            'photo': 'Zdjęcie',
        }

################################################
# Formularz Szkol
class SchoolsForm(forms.ModelForm):
    class Meta:
        model = Schools
        fields = ('name', 'is_available')
        labels = {
            'name': 'Nazwa Szkoły',
            'is_available': 'Dostępna?'
        }

################################################
# Formularz Jezykow
class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        # fields = ('name', 'school_id', 'is_available')
        fields = ('name', 'shortcut', 'level', 'is_available')
        labels = {
            'name': 'Język',
            'shortcut': 'Skrót',
            'level': 'Poziom zaawansowania',
            'is_available': 'Dostępny?'
        }

################################################
# Formularz Przedmiotow
class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        # fields = ('name', 'wage', 'school', 'is_available')
        fields = ('name', 'wage', 'is_available')
        labels = {
            'name': 'Nazwa Przedmiotu',
            'wage': 'Liczba punktów za przedmiot',
            # 'school': 'Szkoła',
            'is_available': 'Dostępny?'
        }

################################################
# Formularz profili
class ProfilesForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ('name', 'school_id', 'is_available')
        labels = {
            'name': 'Nazwa Profilu',
            'school_id': 'Szkoła',
            'is_available': 'Dostępny?'
        }
