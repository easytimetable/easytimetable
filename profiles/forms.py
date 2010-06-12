from django import forms
from profiles.models import ClassGroup, Profile
from locations.models import Campus
from django.contrib.auth.models import User
from django.conf import settings

# it's possible to specify a default password in the settings
# if not is provided, use "password" by default.
DEFAULT_PASSWORD = getattr(settings, 'DEFAULT_PASSWORD', 'password')

class ClassGroupForm(forms.ModelForm):
    class Meta:
        model = ClassGroup

class UserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        return super(UserForm, self).__init__(*args, **kwargs)

    def _create_user(self): 
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
            username = first_name[0].lower() + last_name[:10].lower()
            username.replace(" ", "")
            email = self.cleaned_data['email']
            
            user = User(username=username, 
                email=email)
            user.set_password(DEFAULT_PASSWORD)
            user.save()
            profile = Profile(user=user, first_name=first_name, 
                last_name=last_name)
            return profile

class StudentForm(UserForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    classgroup = forms.ModelChoiceField(queryset=ClassGroup.objects.all())

    def save(self):
        if self.is_valid():
            profile = self._create_user()
            profile.classgroup = self.cleaned_data['classgroup']
            profile.save()
            return profile

    class _meta:
       model = Profile 

class CampusManagerForm(UserForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    campus = forms.ModelChoiceField(queryset=Campus.objects.all())

    def save(self):
        if self.is_valid():
            profile = self._create_user()
            campus = self.cleaned_data['campus']
            profile.campus = campus
            profile.save()
            campus.manager = profile
            campus.save()
            return profile

    class _meta:
        model = Profile

class TeacherForm(UserForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    
    def save(self):
        if self.is_valid():
            profile = self._create_user() 
            profile.is_teacher = True
            profile.save()
            return profile

    class _meta:
        model = Profile
