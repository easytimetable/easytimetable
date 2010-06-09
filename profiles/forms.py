from django import forms
from profiles.models import ClassGroup, Profile
from locations.models import Campus
from django.contrib.auth.models import User
from django.conf import settings

# it's possible to specify a default password in the settings
DEFAULT_PASSWORD = getattr(settings, 'DEFAULT_PASSWORD', 'password')

class ClassGroupForm(forms.ModelForm):
    class Meta:
        model = ClassGroup

class UserForm(forms.Form):
    def _create_user(self, username, first_name, last_name, email): 
            user = User(username=username, 
                first_name=first_name, 
                last_name=last_name, 
                email=email)
            user.set_password(DEFAULT_PASSWORD)
            user.save()
            return user

class StudentForm(UserForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    classgroup = forms.ModelChoiceField(queryset=ClassGroup.objects.all())

    def save(self):
        if self.is_valid():
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
            username = first_name[0].lower() + last_name[:10].lower()
            username.replace(" ", "")
            email = self.cleaned_data['email']
            user = self._create_user(username, first_name, last_name, email)
            
            classgroup = self.cleaned_data['classgroup']
            profile = Profile(classgroup=classgroup, user=user,
            first_name=first_name, last_name=last_name)
            profile.save()
            return profile

class CampusManagerForm(UserForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    campus = forms.ModelChoiceField(queryset=Campus.objects.all())

    def save(self):
        if self.is_valid():
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
            username = first_name[0].lower() + last_name[:10].lower()
            username.replace(" ", "")
            email = self.cleaned_data['email']
            
            user = self._create_user(username, first_name, last_name, email)
            user.save()

            campus = self.cleaned_data['campus']
            profile = Profile(user=user,
            first_name=first_name, last_name=last_name)

            profile.save()
            campus.manager = profile
            campus.save()
            return profile
