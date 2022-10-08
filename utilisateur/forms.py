from django.contrib.auth.forms import User, UserCreationForm
from django import forms
from django.contrib.auth.models import Group

class InscriptionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ConnexionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']

class ModifierUtilisateurForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class GroupeForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
