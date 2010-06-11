from django import forms
from pedagogy.models import Cursus, StudyPeriod, Subject, SubjectModality
from django.contrib.formtools.wizard import FormWizard


class CursusForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class':'datepicker'})
    )
    
    class Meta:
        model = Cursus

class StudyPeriodForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class':'datepicker'})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'class':'datepicker'})
    )
    class Meta:
        model = StudyPeriod

class SubjectForm(forms.ModelForm):
    name = forms.CharField()
    study_period = forms.ModelChoiceField(queryset=StudyPeriod.objects.all())

    def __init__(self, *args, **kwargs):
        """Overwrite the default init method to add as many as needed subject
        modalities.

        """
        super(SubjectForm, self).__init__(*args, **kwargs)
        for (modality_name, real_name) in SubjectModality.TYPE_CHOICES:
            self.fields[modality_name] = forms.CharField(required=False)

    def save(self, *args, **kwargs):
        """Save the form and create the subject modality objects
        
        """
        subject = super(SubjectForm, self).save(*args, **kwargs)
        for (modality, null) in SubjectModality.TYPE_CHOICES:
            sm = SubjectModality(
                planned_hours=self.cleaned_data[modality],
                subject = subject,
                type = modality
            )
            sm.save()

    class Meta:
        model = Subject
