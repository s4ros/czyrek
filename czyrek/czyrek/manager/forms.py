from django import forms

from .models import User

class AddUserPostForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login','passwd','email','full_name','permissions')
