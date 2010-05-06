from django.shortcuts import render_to_response
from django.template import RequestContext

def render_to_response(template_name, context, request, *args, **kwargs):
    """Shortcut for render a response with the context.

    """
    return render_to_response(template_name=template, context,
    context_instance=RequestContext(request), *args, **args)
    
