from django import forms
from profiles.models import ClassGroup, Profile
from django.contrib.auth.models import User

class ClassGroupForm(forms.ModelForm):
    class Meta:
        model = ClassGroup

class StudentForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    classgroup = forms.ChoiceField(
        choices=[(c.id, c.name) for c in ClassGroup.objects.all()])

    def save(self):
        if self.is_valid():
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
            username = first_name[0].lower() + last_name[:10].lower()
            username.replace(" ", "")
            email = self.cleaned_data['email']

            user = User(username=username, 
                first_name=first_name, 
                last_name=last_name, 
                password="password")
            user.save()

            classgroup = self.cleaned_data['classgroup']
            profile = Profile(classgroup_id=classgroup, user=user)
            profile.save()
