from django import forms
from agenda.models import Cursus, StudyPeriod

class CursusForm(forms.ModelForm):
    """The cursus Administration form"""
    
    class Meta:
        model = Cursus

class StudyPeriodForm(forms.ModelForm):
    """The Study Period Administration form"""
    
    class Meta:
        model = StudyPeriod