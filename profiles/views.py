# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# app import
from utils.shortcuts import render_to_response
from utils import crud
from profiles.models import ClassGroup, Profile
from pedagogy.models import Subject
from profiles.forms import ClassGroupForm, StudentForm, CampusManagerForm

@login_required
def add_classgroup(request, campus_id=None):
    if request.POST:
        form = ClassGroupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiles:list_classgroups')
    else:
        form = ClassGroupForm({'campus':campus_id})
    return render_to_response("add_classgroup.html", {
        'form': form,
    }, request)

@login_required
def delete_classgroup(request, classgroup_id):
    classgroup = get_object_or_404(ClassGroup, pk=classgroup_id)
    classgroup.delete()
    request.user.message_set.create(message=_("%s classgroup has been deleted.") % classgroup.name)
    return redirect('profiles:list_classgroups')

@login_required
def list_classgroups(request):
    fields = [('Classe','name'), ('Students', 'profile_set.count'), ('Campus',
    'campus.name')]
    return crud.list(ClassGroup, fields, request, extra_context={
        'form': ClassGroupForm(),
    })

@login_required
def list_classgroup_subjects(request,classgroup_id):
    fields = [('id','id'), ('name', 'name')]
    return crud.list(Subject.objects.filter(
            study_period__cursus__class_group__id=classgroup_id),
            fields, request, obj_name = "")

@login_required
def get_classgroup(request, classgroup_id):
    classgroup = get_object_or_404(ClassGroup, pk=classgroup_id)
    return render_to_response("get_classgroup.html", {
        'classgroup' : classgroup,
    }, request)

@login_required
def update_classgroup(request, classgroup_id):
    classgroup = get_object_or_404(ClassGroup, pk=classgroup_id)
    if request.POST:
        form = ClassGroupForm(data=request.POST, instance=classgroup)
        form.save()
        return redirect('profiles:list_classgroups')
    form = ClassGroupForm(instance=classgroup)
    return render_to_response("add_classgroup.html", {
        'form': form,
    }, request)


# -- User management --------------------------------------------------

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    request.user.message_set.create(message=_("%s user has been deleted.") % user.username)
    return redirect('profiles:list_students')


def list_students(request):
    fields = [('Name', 'username'), ('Class', 'profile_set.get.classgroup.name')]
    return crud.list(User.objects.filter(profile__classgroup__isnull=False), 
        fields, request, obj_name="student", app_name="profiles", 
        extra_context={
            'form': StudentForm(),
            'message': _("When adding a student, the username is " \
            "automatically the first letter of his first name, and" \
            " the rest from this last name. Also, the password is" \
            " always 'password', by default"),
    }, template="list_users.html")

@login_required
def add_student(request):
    if request.POST:
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiles:list_students')
    else:
        form = StudentForm()
    return render_to_response("add_student.html", {
        'form': form,
    }, request)


@login_required
def get_student(request, student_id):
    student = get_object_or_404(User, pk=student_id)
    return render_to_response("get_student.html", {
        'student' : student,
    }, request)

@login_required
def update_student(request, student_id):
    student = get_object_or_404(User, pk=student_id)
    if request.POST:
        form = StudentForm(data=request.POST, instance=student)
        form.save()
        return redirect('profiles:list_students')
    form = StudentForm(instance=student)
    return render_to_response("add_student.html", {
        'form': form,
    }, request)

# -- Campus managers  -----------------------------------------------------

@login_required
def list_campus_managers(request):
    fields = [
        ('First name', 'get_profile.first_name'), 
        ('Last name', 'get_profile.last_name'),
        ('Managed campuses', 'get_profile.list_managed_campuses')]
    return crud.list(
        User.objects.filter(profile__campus_managed__isnull=False).distinct(),
        fields, request, obj_name="campus_manager", app_name="profiles", 
        extra_context={
            'form': CampusManagerForm(),
            'message': _("When adding a campus manager, the username is " \
            "automatically the first letter of his first name, and" \
            " the rest from this last name. Also, the password is" \
            " always 'password', by default"),
            'obj_verbose_name': "Campus manager"
    }, template="list_campus_managers.html")

@login_required
def add_campus_manager(request):
    if request.POST:
        form = CampusManagerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiles:list_campus_managers')
    else:
        form = StudentForm()
    return render_to_response("add_campus_manager.html", {
        'form': form,
    }, request)

@login_required
def get_campus_manager(request, campus_manager_id):
    campus_manager = get_object_or_404(User, pk=campus_manager_id)
    return render_to_response("get_campus_manager.html", {
        'campus_manager' : campus_manager,
    }, request)

def delete_campus_manager(request, user_id):
    profile = Profile.objects.get(user__id=user_id) 
    profile.campus_managed.clear()
    return redirect('profile:list_campus_manager')

@login_required
def update_campus_manager(request, campus_manager_id):
    campus_manager = get_object_or_404(User, pk=campus_manager_id)
    if request.POST:
        form = StudentForm(data=request.POST, instance=campus_manager)
        form.save()
        return redirect('profiles:list_campus_managers')
    form = StudentForm(instance=campus_manager)
    return render_to_response("add_campus_manager.html", {
        'form': form,
    }, request)
