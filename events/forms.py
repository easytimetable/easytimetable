from django import forms
from events.models import Event
from profiles.models import ClassGroup
from utils.widgets import SelectableTimeWidget

class UserEventForm(forms.Form):
    name = forms.CharField(label="Event name")
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    start_hour = forms.IntegerField(widget=SelectableTimeWidget())
    duration = forms.IntegerField(widget=SelectableTimeWidget(end_hour=5))
    place_text = forms.CharField(label="Place", required=False)

#capitaine skeletor pour le reste des forms du campus manager
class ClassgroupEventForm(forms.Form):
    name = forms.CharField(label="Event name")
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    start_hour = forms.IntegerField(widget=SelectableTimeWidget())
    duration = forms.IntegerField(widget=SelectableTimeWidget(end_hour=5))
    place_text = forms.CharField(label="Place", required=False)

class CampusEventForm(forms.Form):
    name = forms.CharField(label="Event name")
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    start_hour = forms.IntegerField(widget=SelectableTimeWidget())
    duration = forms.IntegerField(widget=SelectableTimeWidget(end_hour=5))
    place_text = forms.CharField(label="Place", required=False)

class MoveEventForm(forms.Form):
    days = forms.IntegerField()
    minutes = forms.IntegerField()
    all_day = forms.BooleanField()


class ClassgroupSelectorForm(forms.Form):
    user = None
    classgroup = forms.ModelChoiceField(queryset=None)
    def __init__(self, user=None, *args, **kwargs):
        super(ClassgroupSelectorForm,self).__init__(*args, **kwargs)
        self.user = user
        self.fields['classgroup'].queryset = ClassGroup.objects.get_managed(self.user)

