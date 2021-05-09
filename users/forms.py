from django import forms
from users.models import AddUser


class UserForm(forms.ModelForm):
    class Meta:
        model =AddUser
        fields = [
            'username',
            'email',
        ]
