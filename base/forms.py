from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserCreationForm(UserCreationForm):
    class Meta:
        model = Investor
        fields = ['email', 'username', 'identity_fin', 'contact_num', 'password1', 'password2']