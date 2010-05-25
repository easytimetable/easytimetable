from django import forms
from agenda.models import Cursus, StudyPeriod, Subject, SubjectModality, ClassGroup

class CursusForm(forms.ModelForm):
    """The cursus Administration form"""
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class':'datepicker'})
    )
    
    class Meta:
        model = Cursus

class StudyPeriodForm(forms.ModelForm):
    """The Study Period Administration form"""
    
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class':'datepicker'})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'class':'datepicker'})
    )
    class Meta:
        model = StudyPeriod

class SubjectForm(forms.ModelForm):
    """The Subject Administration form"""
    name = forms.CharField()
    study_period = forms.ModelChoiceField(queryset=StudyPeriod.objects.all())

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        for (modality_name, real_name) in SubjectModality.TYPE_CHOICES:
            self.fields[modality_name] = forms.CharField()

    class Meta:
        model = Subject

class SubjectModalityForm(forms.ModelForm):
    """The Subject Modality Administration form"""
    
    class Meta:
        model = SubjectModality

class ClassGroupForm(forms.ModelForm):
    """The classgroup form"""
    
    class Meta:
        model = ClassGroup
