from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Technique


list_of_categories = (
    ('BLOCKS', 'Blocks'),
    ('BUNKAI', 'Bunkai'),
    ('FORMS', 'Forms'),
    ('KEMPOS', 'Kempos'),
    ('OTHER', 'Other'),
    ('STRIKES', 'Strikes'),
    ('WEAPONS', 'Weapons')
)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddTechnique(forms.Form):
    technique = forms.CharField(max_length=50)
    category = forms.ChoiceField(choices=list_of_categories)
    notes = forms.CharField(widget=forms.Textarea, required=False)
