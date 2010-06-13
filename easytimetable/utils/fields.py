from django import forms

class UserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_profile()
