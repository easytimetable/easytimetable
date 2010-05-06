from agenda.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

def get_campus(request, campus_id):
    campus = get_object_or_404(Campus, pk = campus_id)
    return render_to_response('agenda/campuses/get.html',
                              { 'campus' : campus }, 
                              request)

def delete_campus(request, campus_id):
    campus = get_object_or_404(Campus, pk = campus_id)
    pass

def update_campus(request, campus_id):
    campus = get_object_or_404(Campus, pk = campus_id)
    pass

def add_campus(request):
    pass

def list_campuses(request):
    pass
