from django import forms
from .models import Celeb


class Celebform(forms.ModelForm):
    class Meta:
        model = Celeb
        fields = ['name', 'age', 'info', 'image']