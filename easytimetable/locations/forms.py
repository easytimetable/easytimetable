from django import forms
from django.utils.translation import ugettext_lazy as _
from locations.models import University, Campus, Place

class UniversityForm(forms.ModelForm):
    """The university form"""
    
    class Meta:
        model = University

class CampusForm(forms.ModelForm):
    """The campus form"""
    address = forms.CharField(required=False) 
    
    def __init__(self, *args, **kwargs):
        super(CampusForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs.keys():
            try:
                place = Place.objects.get(is_main_place=True, 
                    campus=kwargs['instance'])
                self.fields['address'].initial = place.address
                self.fields['address'].help_text = _(
                    "Don't touch this to let the actual value")
            except Place.DoesNotExist:
                pass
        
    
    def save(self, *args, **kwargs):
        """Create/Update the main place when needed"""
        campus = super(CampusForm, self).save(*args, **kwargs)
        
        address = self.cleaned_data['address']
        if address != "":
            # find for a place with this adress
            try:
                places = Place.objects.filter(campus=campus, is_main_place=True)
                main_place = places[0]
                main_place.campus = campus 
            except IndexError:
                # if none found, create one.
                main_place = Place(name=campus.name, 
                address=address, is_main_place=True, campus=campus)
            main_place.save()
        return campus

    class Meta:
        model = Campus

class PlaceForm(forms.ModelForm):

    """The place form"""

    class Meta:
        model = Place
