from django import forms
from agenda.models import University, Campus

class UniversityForm(forms.ModelForm):
    """The university form"""
    
    class Meta:
        model = University

class CampusForm(forms.ModelForm):
    """The campus form"""
    
    class Meta:
        model = Campus
