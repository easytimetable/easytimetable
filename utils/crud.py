from utils.shortcuts import render_to_response
from utils.settings import DEFAULT_LIST_TEMPLATE

def list(obj_class, cols, request, template=DEFAULT_LIST_TEMPLATE, 
        obj_name=None, app_name=None, extra_context={}):
    objs = obj_class.objects.all()
    list_params = {}
    if objs:
        for obj in objs:
            list_params[obj.id] = []
            for (key, attrs) in cols:
                item = obj
                for attr in attrs.split('.'):
                    if hasattr(item, attr):
                        item = getattr(item, attr)
                        if callable(item):
                            try:
                                item = item()
                            except Exception:
                                item = ""
                    else:
                        item = ""
                list_params[obj.id].append((key, item))
    if obj_name is None:
        obj_name = obj_class.__name__.lower()
    if app_name is None:
        app_name = obj_class.__module__.split('.')[0]

    return_context = {
        'elements': list_params,
        'obj_name': obj_name,
        'app_name': app_name,
    }

    for key, value in extra_context.items():
        return_context[key] = value
    return render_to_response(template, return_context, request)
