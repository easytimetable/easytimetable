from django import forms
from agenda.models import ClassGroup

class ClassGroupForm(forms.ModelForm):
    """The classgroup form"""
    
    class Meta:
        model = ClassGroup
