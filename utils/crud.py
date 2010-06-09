from utils.shortcuts import render_to_response
from utils.settings import DEFAULT_LIST_TEMPLATE
from django.db.models.query import QuerySet
from django.db.models.base import ModelBase
from django.utils import simplejson as json
from django.http import HttpResponse



def list(queryset, cols, request, template=DEFAULT_LIST_TEMPLATE, 
        obj_name=None, app_name=None, extra_context={}):

    if isinstance(queryset, QuerySet):
        objs = queryset
    elif isinstance(queryset, ModelBase):
        objs = queryset.objects.all()

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
        obj_name = queryset.__name__.lower()
    if app_name is None:
        app_name = queryset.__module__.split('.')[0]
    
    #Gruik
    if request.is_ajax():
        return HttpResponse(json.dumps([dict(list_params[m]) 
                            for m in list_params]))

    return_context = {
        'elements': list_params,
        'obj_name': obj_name,
        'app_name': app_name,
        'obj_verbose_name': extra_context.setdefault(
            "obj_verbose_name", obj_name),
    }

    for key, value in extra_context.items():
        return_context[key] = value
    return render_to_response(template, return_context, request)
