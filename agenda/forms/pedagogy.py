from django import forms
from agenda.models import Cursus, StudyPeriod, Subject

class CursusForm(forms.ModelForm):
    """The cursus Administration form"""
    
    class Meta:
        model = Cursus

class StudyPeriodForm(forms.ModelForm):
    """The Study Period Administration form"""
    
    class Meta:
        model = StudyPeriod

class SubjectForm(forms.ModelForm):
    """The Subject Administration form"""
    
    class Meta:
        model = Subject