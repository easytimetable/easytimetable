from django import forms
from locations.models import University, Campus, Place

class UniversityForm(forms.ModelForm):
    """The university form"""
    
    class Meta:
        model = University

class CampusForm(forms.ModelForm):
    """The campus form"""
    address = forms.CharField(required=False)
    
    def save(self, *args, **kwargs):
        """Create/Update the main place when needed"""
        campus = super(CampusForm, self).save(*args, **kwargs)
        
        address = self.cleaned_data['address']
        if address is not None:
            main_place = Place(name=campus.name, 
                address=address, is_main_place=True, campus=campus)
            main_place.save()

    class Meta:
        model = Campus

class PlaceForm(forms.ModelForm):

    """The place form"""

    class Meta:
        model = Place
