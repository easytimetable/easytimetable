from django import forms
from agenda.models import Event
from utils.widgets import SelectableTimeWidget

class UserEventForm(forms.Form):
    name = forms.CharField(label="Event name")
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    start_hour = forms.IntegerField(widget=SelectableTimeWidget())
    duration = forms.IntegerField(widget=SelectableTimeWidget(end_hour=5))
    place_text = forms.CharField(label="Place", required=False)

class ClassEventForm(forms.Form):
    def __init__(self, classgroup=None, cursus=None, campus=None, 
        university=None, *args, **kwargs):
        if classgroup:
            pass

class MoveEventForm(forms.Form):
    days = forms.IntegerField()
    minutes = forms.IntegerField()
    all_day = forms.BooleanField()
