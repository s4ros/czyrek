from django import forms

from .models import User, Candidate

#############################################3
## Formularz dodawania uzytkownikow
class AddUserPostForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login','passwd','email','full_name','permissions',)


#############################################3
## Formularz logowania - homepage
class LoginForm(forms.ModelForm):
    passwd = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('login','passwd',)

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
