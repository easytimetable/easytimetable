from django import forms
from events.models import Event
from profiles.models import ClassGroup
from pedagogy.models import Subject, SubjectModality
from locations.models import Place, Campus
from events.models import Who, When, Event
from datetime import date, datetime, timedelta
from utils.widgets import SelectableTimeWidget

class UserEventForm(forms.Form):
    name = forms.CharField(label="Event name")
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    start_hour = forms.IntegerField(widget=SelectableTimeWidget())
    duration = forms.IntegerField(widget=SelectableTimeWidget(end_hour=5))
    place_text = forms.CharField(label="Place", required=False)

#capitaine skeletor pour le reste des forms du campus manager
class ClassgroupEventForm(forms.Form):
    user = None
    classgroup = forms.ModelChoiceField(queryset=None, label="Class")
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(),
                                     label="Subject")
    name = forms.CharField(label="Event name")
    modality = forms.CharField(max_length=20,
                widget=forms.Select(choices=SubjectModality.TYPE_CHOICES))
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    start_hour = forms.IntegerField(widget=SelectableTimeWidget())
    duration = forms.IntegerField(widget=SelectableTimeWidget(end_hour=5))
    place_text = forms.CharField(label="Place T", required=False)
    place = forms.ModelChoiceField(queryset=None, label="Place")
    
    def __init__(self, user=None, *args, **kwargs):
        super(ClassgroupEventForm,self).__init__(*args, **kwargs)
        self.user = user
        self.fields['classgroup'].queryset = ClassGroup.objects.get_managed_by(self.user)
        self.fields['place'].queryset = Place.objects.get_managed_by(self.user)

    def save(self): 
        if self.is_valid(): 
            f = self.cleaned_data 
            subject_modality = SubjectModality.objects.filter( 
                               subject=f['subject']).filter( 
                               type=f['modality']).get() 
            event = Event(name=f['name'], 
                          duration=f['duration'],  
                          place_text=f['place_text'], 
                          subject_modality=subject_modality) 
            event.save() 
            event.places.add(f['place']) 
            who = Who(classgroup=f['classgroup'], event=event) 
            who.save() 
            edate = "%s %s" % (f['date'], 
                f['start_hour']) 
            edate = datetime.strptime(edate, "%Y-%m-%d %H") 
            when = When(date=edate, event=event) 
            when.save()
            return when
        return False
 

class CampusEventForm(forms.Form):
    user = None
    
    campus = forms.ModelChoiceField(queryset=None,
                                     label="Campus", required=False)
    name = forms.CharField(label="Event name")
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    start_hour = forms.IntegerField(widget=SelectableTimeWidget())
    duration = forms.IntegerField(widget=SelectableTimeWidget(end_hour=5))
    place_text = forms.CharField(label="Place", required=False)
    place = forms.ModelChoiceField(queryset=None,
                                     label="Place", required=False)
    
    def __init__(self, user=None, *args, **kwargs):
        super(CampusEventForm,self).__init__(*args, **kwargs)
        self.user = user
        self.fields['place'].queryset = Place.objects.get_managed_by(self.user)
        self.fields['campus'].queryset = Campus.objects.get_managed_by(self.user)

    def save(self):
        if self.is_valid():
            f = self.cleaned_data
            event = Event(name=f['name'],
                          duration=f['duration'],
                          place_text=f['place_text'],)
            event.save()
            if f['place']:
                event.places.add(f['place'])
            who = Who(campus=f['campus'], event=event)
            who.save()
            edate = "%s %s" % (f['date'],
                f['start_hour'])
            edate = datetime.strptime(edate, "%Y-%m-%d %H")
            when = When(date=edate, event=event)
            when.save()
            return when
        return False



class MoveEventForm(forms.Form):
    days = forms.IntegerField()
    minutes = forms.IntegerField()
    all_day = forms.BooleanField()

class CampusSelectorForm(forms.Form):
    user = None
    campus = forms.ModelMultipleChoiceField(queryset=None)
    def __init__(self, user=None, *args, **kwargs):
        super(CampusSelectorForm,self).__init__(*args, **kwargs)
        self.user = user
        self.fields['campus'].queryset = Campus.objects.get_managed_by(self.user)

class ClassgroupSelectorForm(forms.Form):
    user = None
    classgroup = forms.ModelMultipleChoiceField(queryset=None)
    def __init__(self, user=None, *args, **kwargs):
        super(ClassgroupSelectorForm,self).__init__(*args, **kwargs)
        self.user = user
        self.fields['classgroup'].queryset = ClassGroup.objects.get_managed_by(self.user)

