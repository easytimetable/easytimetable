# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

# app import
from agenda.views import render_to_response
from agenda.models import University, Campus, Place
from agenda.forms import UniversityForm, CampusForm, PlaceForm


"""Campus
"""

@login_required
def add_campus(request):
    if request.POST:
        form = CampusForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:list_campuses')
    else:
        form = CampusForm()

    return render_to_response("agenda/locations/add_campus.html", {
        'form': form,
    }, request)

@login_required
def delete_campus(request, campus_id):
    campus = get_object_or_404(Campus, pk=campus_id)
    campus.delete()
    request.user.message_set.create(message=_("%s campus has been deleted.") % campus.name)
    return redirect('agenda:list_universities')

@login_required
def get_campus(request, campus_id):
    campus = get_object_or_404(Campus, pk=campus_id)
    return render_to_response('agenda/locations/get_campus.html',
                              { 'campus' : campus }, 
                              request)

@login_required
def list_campuses(request):
    campuses = Campus.objects.all()
    return render_to_response("agenda/locations/list_campuses.html", {
        'campuses': campuses,
    }, request)


@login_required
def update_campus(request, campus_id):
    campus = get_object_or_404(Campus, pk=campus_id)
    if request.POST:
        form = CampusForm(data=request.POST, instance=campus)
        form.save()
        return redirect('agenda:list_campuses')
    form = CampusForm(instance=campus)
    return render_to_response("agenda/locations/add_campus.html", {
        'form': form,
    }, request)


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

@login_required	
def get_university(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    return render_to_response('agenda/locations/get_university.html',
                              { 'university' : university },
                              request)

@login_required
def list_universities(request):
    universities = University.objects.all()
    return render_to_response("agenda/locations/list_universities.html", {
        'universities': universities,
    }, request)

@login_required
def update_university(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    if request.POST:
        form = UniversityForm(data=request.POST, instance=university)
        form.save()
        return redirect('agenda:list_universities')
    form = UniversityForm(instance=university)
    return render_to_response("agenda/locations/add_university.html", {
        'form': form,
    }, request)


"""Places
"""

@login_required
def add_place(request):
    if request.POST:
        form = PlaceForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:list_places')
    else:
        form = PlaceForm()

    return render_to_response("agenda/locations/add_place.html", {
        'form': form,
    }, request)

@login_required
def delete_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place.delete()
    request.user.message_set.create(message=_("%s university has been deleted.") % place.name)
    return redirect('agenda:list_places')

@login_required
def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return render_to_response('agenda/locations/get_place.html',
                              { 'place' : place },
                              request)

@login_required
def list_places(request):
    places = Place.objects.all()
    return render_to_response("agenda/locations/list_places.html", {
        'places': places,
    }, request)


@login_required
def update_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if request.POST:
        form = PlaceForm(data=request.POST, instance=place)
        form.save()
        return redirect('agenda:list_places')
    form = PlaceForm(instance=place)
    return render_to_response("agenda/locations/add_place.html", {
        'form': form,
    }, request)
