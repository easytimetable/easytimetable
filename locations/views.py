@login_required
def list_places(request, campus_id=None):
    if request.is_ajax():
        fields = 
        return crud.list(Place.objects.filter(campus_id=campus_id), fields, request)
    fields = [('Place', 'name'), ('Campus', 'campus.name')]
    return crud.list(Place, fields, request, extra_context={
        'form': PlaceForm(),
    })
