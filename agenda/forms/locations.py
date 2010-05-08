from django import forms
from agenda.models import University

class UniversityForm(forms.ModelForm):
    """The university form"""
    
    class Meta:
        model = University
