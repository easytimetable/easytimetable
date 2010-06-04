from django import forms
from locations.models import University, Campus, Place

class UniversityForm(forms.ModelForm):
    """The university form"""
    
    class Meta:
        model = University

class CampusForm(forms.ModelForm):
    """The campus form"""
    
    class Meta:
        model = Campus

class PlaceForm(forms.ModelForm):

    """The place form"""

    class Meta:
        model = Place
