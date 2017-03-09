from django import forms

from .models import User

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
