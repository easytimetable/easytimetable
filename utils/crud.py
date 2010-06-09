from django.db.models.query import QuerySet
from django.db.models.base import ModelBase
from django.utils import simplejson as json
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse

from django.views.generic.create_update import get_model_and_form_class, create_object, update_object
from django.views.generic.list_detail import object_detail

from utils.shortcuts import render_to_response
from utils.settings import DEFAULT_LIST_TEMPLATE

def create(request, post_save_redirect, *args, **kwargs):
    """thin wrapper around django generic view to support reverse urls
    """
    return create_object(request=request,
        post_save_redirect=reverse(post_save_redirect), *args, **kwargs)

def update(request, post_save_redirect, *args, **kwargs):
    """thin wrapper around django generic view to support reverse  urls
    """
    return update_object(request=request, 
        post_save_redirect=reverse(post_save_redirect), *args, **kwargs)

def get(*args, **kwargs):
    """thin wrapper around django generic view to support reverse  urls
    """
    return object_detail(*args, **kwargs) 

def delete(request, model, object_id, post_delete_redirect, verbose_name="object", 
    field_name='id'):
    """Delete an object
    """
    object = get_object_or_404(model, pk=object_id)
    request.user.message_set.create(message=_("%s %s has been deleted.") %(
            getattr(object, field_name, 'The'), verbose_name))
    object.delete()
    return redirect(post_delete_redirect)

def list(request, fields, model=None, queryset=None, form_class=None, 
        template=DEFAULT_LIST_TEMPLATE, object_name=None, app_name=None, 
        object_verbose_name=None, extra_context={}):
    """A generic List method, that allows to specify the list of what we want
    to display.
    """
    model, form_class = get_model_and_form_class(model, form_class) 
    if queryset is not None:
        queryset = queryset
    else:
        queryset = model.objects.all()

    list_params = {}
    if queryset:
        for obj in queryset:
            list_params[obj.id] = []
            for (key, attrs) in fields:
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
    if object_name is None:
        object_name = model.__name__.lower()
    if app_name is None:
        app_name = model.__module__.split('.')[0]
    
    #Gruik
    if request.is_ajax():
        return HttpResponse(json.dumps([dict(list_params[m]) 
                            for m in list_params]))

    return_context = {
        'elements': list_params,
        'object_name': object_name,
        'app_name': app_name,
        'object_verbose_name': object_verbose_name or object_name,
        'form': form_class(),
    }

    for key, value in extra_context.items():
        return_context[key] = value
    return render_to_response(template, return_context, request)
