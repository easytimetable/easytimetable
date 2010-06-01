from django import forms
from agenda.models import Event
from utils.widgets import SelectableTimeWidget

class UserEventForm(forms.Form):
    name = forms.CharField(label="Event name")
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    start_hour = forms.TimeField(widget=SelectableTimeWidget())
    duration = forms.TimeField(widget=SelectableTimeWidget(end_hour=5),
                    help_text="in hours")
    place_text = forms.CharField(label="Place", required=False)

class ClassEventForm(forms.Form):
    def __init__(self, classgroup=None, cursus=None, campus=None, 
        university=None, *args, **kwargs):
        if classgroup:
            pass
