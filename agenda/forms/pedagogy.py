from django import forms
from agenda.models import Cursus

class CursusForm(forms.ModelForm):
    """The cursus classgroup form"""
    
    class Meta:
        model = Cursus
