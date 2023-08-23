from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    class Metta:
        model = Place 
        field = ['nname', 'location', 'description']