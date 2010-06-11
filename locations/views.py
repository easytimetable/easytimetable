@login_required
def list_places(request, campus_id=None):
    if request.is_ajax():
        fields = [('id','id'), ('name', 'name')]
        return crud.list(queryset=Place.objects.filter(campus_id=campus_id),
                         fields=fields, 
                         request=request)
    fields = [('Place', 'name'), ('Campus', 'campus.name')]
    return crud.list(Place, fields, request, extra_context={
        'form': PlaceForm(),
    })
