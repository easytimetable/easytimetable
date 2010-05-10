# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

# app import
from agenda.views import render_to_response
from agenda.models import University
from agenda.forms import UniversityForm

def get_campus(request, campus_id):
    campus = get_object_or_404(Campus, pk=campus_id)
    return render_to_response('agenda/campuses/get.html',
                              { 'campus' : campus }, 
                              request)
@login_required
def delete_campus(request, campus_id):
    campus = get_object_or_404(Campus, pk=campus_id)
    pass

@login_required
def update_campus(request, campus_id):
    campus = get_object_or_404(Campus, pk=campus_id)
    pass

def add_campus(request):
    pass

def list_campuses(request):
    pass
"""University
"""

@login_required
def add_university(request):
    if request.POST:
        form = UniversityForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:list_universities')
    else:
        form = UniversityForm()

    return render_to_response("agenda/locations/add_university.html", {
        'form': form,
    }, request)
        

@login_required
def delete_university(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    university.delete()
    request.user.message_set.create(message=_("%s university has been deleted.") % university.name)
    return redirect('agenda:list_universities')

def update_university(request, university_id):
	"""
	"""
	
def get_university(request):
	"""
	"""
	
@login_required
def list_universities(request):
    universities = University.objects.all()
    return render_to_response("agenda/locations/list_universities.html", {
        'universities': universities,
    }, request)

"""Places
"""

def add_place(request):
    pass

def delete_place(request, place_id):
    pass

def update_place(request, place_id):
    pass

def list_places(request):
    pass

def get_place(request, place_id):
    pass
