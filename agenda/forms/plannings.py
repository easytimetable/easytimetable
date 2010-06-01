from django import forms
from agenda.models import Event

class UserEventForm(forms.Form):
    name = forms.CharField(label="Event name")
    date = forms.DateTimeField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    duration = forms.IntegerField(label="Event duration", help_text="in hours")
    place_text = forms.CharField(label="Place", required=False)

class ClassEventForm(forms.Form):
    def __init__(self, classgroup=None, cursus=None, campus=None, 
        university=None, *args, **kwargs):
        if classgroup:
            pass
