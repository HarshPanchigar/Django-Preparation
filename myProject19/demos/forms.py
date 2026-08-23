from django import forms
from .models import Person

class NameForm(forms.Form):
    class Meta:
        model = Person
        feilds = ['name']