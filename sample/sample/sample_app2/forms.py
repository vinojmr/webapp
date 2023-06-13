from django import forms
from .models import Actor

class Actor_form(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'age', 'about', 'image']
