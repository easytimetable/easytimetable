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

    def _build_event(self, old_when=None):
        if self.is_valid():
            old_id = None
            if old_when:
                old_id = old_when.event.id
            event = Event(name=self.cleaned_data['name'],
                          duration=self.cleaned_data['duration'],
                          place_text=self.cleaned_data['place_text'],
                          id=old_id)
            return event

    def _build_when(self, old_when=None):
        if self.is_valid():
            old_id = None
            if old_when:
                old_id = old_when.id
            correct_date = "%s %s" % (self.cleaned_data['date'],
                self.cleaned_data['start_hour'])
            correct_date = datetime.strptime(correct_date, "%Y-%m-%d %H")
            when = When(date=correct_date, id=old_id)
            return when

    def save(self, when=None):
        if self.is_valid():
            event = self._build_event(when)
            when = self._build_when(when)
            event.save()
            when.event = event
            when.save()
            return when
        return False
    

        

#capitaine skeletor pour le reste des forms du campus manager
class ClassgroupEventForm(UserEventForm):
    user = None
    classgroup = forms.ModelChoiceField(queryset=None, label="Class")
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(),
                                     label="Subject")
    modality = forms.CharField(max_length=20,
                widget=forms.Select(choices=SubjectModality.TYPE_CHOICES))
    place = forms.ModelChoiceField(queryset=None, label="Place")
    
    def __init__(self, user=None, *args, **kwargs):
        super(ClassgroupEventForm,self).__init__(*args, **kwargs)
        self.user = user
        self.fields['classgroup'].queryset = ClassGroup.objects.get_managed_by(self.user)
        self.fields['place'].queryset = Place.objects.get_managed_by(self.user)
    
    def _build_classgroup(self, old_when=None):
        if self.is_valid():
            old_id = None
            if old_when:
                old_id = old_when.event.who_set.get(classgroup__isnull=False).id
            return Who(classgroup=self.cleaned_data['classgroup'], id=old_id)

    def save(self, when=None): 
        if self.is_valid(): 
            f = self.cleaned_data 
            event = self._build_event(when)
            event.subject_modality = SubjectModality.objects.filter( 
                               subject=f['subject']).filter( 
                               type=f['modality']).get() 
            event.save() 
            event.places.clear()
            event.places.add(f['place']) 
            who = self._build_classgroup(when)
            who.event = event
            who.save() 
            when = self._build_when(when)
            when.event = event
            when.save()
            return when
        return False

class CampusEventForm(UserEventForm):
    user = None
    
    campus = forms.ModelChoiceField(queryset=None,
                                     label="Campus", required=False)
    place = forms.ModelChoiceField(queryset=None,
                                     label="Place", required=False)
    
    def __init__(self, user=None, *args, **kwargs):
        super(CampusEventForm,self).__init__(*args, **kwargs)
        self.user = user
        self.fields['place'].queryset = Place.objects.get_managed_by(self.user)
        self.fields['campus'].queryset = Campus.objects.get_managed_by(self.user)

    def _build_campus(self, old_when=None):
        if self.is_valid():
            old_id = None
            if old_when:
                old_id = old_when.event.who_set.get(campus__isnull=False).id
            return Who(campus=self.cleaned_data['campus'], id=old_id)

    def save(self, when=None):
        if self.is_valid():
            event = self._build_event(when)
            event.save()
            who = self._build_campus(when)
            who.event = event
            who.save()
            when = self._build_when(when)
            when.event = event
            when.save()
            return when
        return False
    
class MoveEventForm(forms.Form):
    days = forms.IntegerField()
    minutes = forms.IntegerField()
    all_day = forms.BooleanField()

    
class MySelectorForm(forms.Form):
    user = None
    calendars = forms.MultipleChoiceField(choices=
        [("my_campus", "My Campus"),
         ("my_classgroup", "My Class"),
         ("my_user", "Mine")],
        widget=forms.CheckboxSelectMultiple())
    def __init__(self, what=[], *args, **kwargs):
        super(MySelectorForm,self).__init__(*args, **kwargs)
        if what == []:
            return
        new_choices = []
        for option in self.fields['calendars'].choices:
            if option[0] in what:
                new_choices.append(option)
        self.fields['calendars'].choices = new_choices

class CampusSelectorForm(forms.Form):
    user = None
    campus = forms.ModelMultipleChoiceField(queryset=None,
            widget=forms.CheckboxSelectMultiple())
    def __init__(self, user=None, *args, **kwargs):
        super(CampusSelectorForm,self).__init__(*args, **kwargs)
        self.user = user
        self.fields['campus'].queryset =\
            Campus.objects.get_managed_by(self.user)

class ClassgroupSelectorForm(forms.Form):
    user = None
    classgroup = forms.ModelMultipleChoiceField(queryset=None,
                widget=forms.CheckboxSelectMultiple())
    def __init__(self, user=None, *args, **kwargs):
        super(ClassgroupSelectorForm,self).__init__(*args, **kwargs)
        self.user = user
        self.fields['classgroup'].queryset =\
            ClassGroup.objects.get_managed_by(self.user)

