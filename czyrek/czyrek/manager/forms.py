from django import forms

from .models import Candidate
from django.contrib.auth.models import User

#############################################3
## Formularz dodawania uzytkownikow
class AddUserPostForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name','is_staff','is_active',)

#############################################3
## Formularz logowania - homepage
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password',)

#############################################3
## Forularz dodawania Kandydata
# class CandidateAddForm(forms.ModelForm):
#     # TODO: Define other fields here
#     class Meta:
#         model = Candidate
#         fields = ('name', 'surname', 'city', 'address', 'postalcode',
#                   'voivodeship', 'community', 'phone', 'pesel',
#                   'birthdate', 'last_school', 'primary_language',
#                   'secondary_language', 'subject_one', 'subject_two',
#                   'subject_three', 'photo')
