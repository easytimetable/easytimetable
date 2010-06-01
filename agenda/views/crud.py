from agenda.views import render_to_response

def list(obj_class, cols, request, template="list.html", obj_name=None, app_name=None):
    objs = obj_class.objects.all()
    list_params = {}
    if objs:
        for obj in objs:
            list_params[obj.id] = []
            for (key, attrs) in cols:
                item = obj
                for attr in attrs.split('.'):
                    item = getattr(item, attr)
                    if callable(item):
                        item = item()
                list_params[obj.id].append((key, item))
    if obj_name is None:
        obj_name = obj_class.__name__.lower()
    if app_name is None:
        app_name = obj_class.__module__.split('.')[0]
    return render_to_response(template, {
        'elements': list_params,
        'obj_name': obj_name,
        'app_name': app_name,
    }, request)

