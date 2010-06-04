from django import forms
from profiles.models import ClassGroup

class ClassGroupForm(forms.ModelForm):
    class Meta:
        model = ClassGroup
