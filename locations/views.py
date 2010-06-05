# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

# app import
from utils.shortcuts import render_to_response
from utils import crud
from locations.models import University, Campus, Place
from locations.forms import UniversityForm, CampusForm, PlaceForm

# -- Campuses ----------------------------------------------------------

@login_required
def add_campus(request):
    if request.POST:
        form = CampusForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('locations:list_campuses')
    else:
        form = CampusForm()

    return render_to_response("add_campus.html", {
        'form': form,
    }, request)

@login_required
def delete_campus(request, campus_id):
    campus = get_object_or_404(Campus, pk=campus_id)
    campus.delete()
    request.user.message_set.create(message=_("%s campus has been deleted.") % campus.name)
    return redirect('locations:list_universities')

@login_required
def get_campus(request, campus_id):
    campus = get_object_or_404(Campus, pk=campus_id)
    return render_to_response('get_campus.html',
                              { 'campus' : campus }, 
                              request)

@login_required
def list_campuses(request):
    fields = [('Campus', 'name'), ('University', 'university.name')]
    return crud.list(Campus, fields, request, extra_context={
        'form': CampusForm(),
        'message': _("If you specify an address here, it will automatically" \
            "create a new place and set it the main place for this campus")
    })

@login_required
def update_campus(request, campus_id):
    campus = get_object_or_404(Campus, pk=campus_id)
    if request.POST:
        form = CampusForm(data=request.POST, instance=campus)
        form.save()
        return redirect('locations:list_campuses')
    form = CampusForm(instance=campus)
    return render_to_response("add_campus.html", {
        'form': form,
    }, request)

# -- Universities --------------------------------------------------

@login_required
def add_university(request):
    if request.POST:
        form = UniversityForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('locations:list_universities')
    else:
        form = UniversityForm()

    return render_to_response("add_university.html", {
        'form': form,
    }, request)
        
@login_required
def delete_university(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    university.delete()
    request.user.message_set.create(message=_("%s university has been deleted.") % university.name)
    return redirect('locations:list_universities')

@login_required    
def get_university(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    return render_to_response('get_university.html',
                              { 'university' : university },
                              request)

@login_required
def list_universities(request):
    fields = [('University', 'name'), ('Campus', 'campus_set.count')]
    return crud.list(University, fields, request, extra_context={
        'form': UniversityForm(),
    })

@login_required
def update_university(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    if request.POST:
        form = UniversityForm(data=request.POST, instance=university)
        form.save()
        return redirect('locations:list_universities')
    form = UniversityForm(instance=university)
    return render_to_response("add_university.html", {
        'form': form,
    }, request)


# -- Places ------------------------------------------------------------------

@login_required
def add_place(request):
    if request.POST:
        form = PlaceForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('locations:list_places')
    else:
        form = PlaceForm()

    return render_to_response("add_place.html", {
        'form': form,
    }, request)

@login_required
def delete_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place.delete()
    request.user.message_set.create(message=_("%s university has been deleted.") % place.name)
    return redirect('locations:list_places')

@login_required
def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return render_to_response('get_place.html',
                              { 'place' : place },
                              request)

@login_required
def list_places(request):
    fields = [('Place', 'name'), ('Campus', 'campus.name')]
    return crud.list(Place, fields, request, extra_context={
        'form': PlaceForm(),
    })

@login_required
def update_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if request.POST:
        form = PlaceForm(data=request.POST, instance=place)
        form.save()
        return redirect('locations:list_places')
    form = PlaceForm(instance=place)
    return render_to_response("add_place.html", {
        'form': form,
    }, request)
