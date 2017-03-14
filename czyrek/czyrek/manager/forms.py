from django import forms

from .models import Candidate
from django.contrib.auth.models import User

#############################################3
## Formularz dodawania uzytkownikow
class AddUserPostForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name','is_staff','is_active',)


#############################################3
## Formularz logowania - homepage
class LoginForm(forms.ModelForm):
    passwd = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password',)

#############################################3
## Forularz dodawania Kandydata
class CandidateAddForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Candidate
        fields = []

    def __init__(self, *args, **kwargs):
        super(CandidateAddForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CandidateAddForm, self).clean()
        return cleaned_data
