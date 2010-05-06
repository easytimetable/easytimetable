from django.shortcuts import render_to_response as base_render_to_response
from django.template import RequestContext

def render_to_response(template_name, context, request=None):
    """Shortcut for render a response with the context.

    """
    return base_render_to_response(template_name, context,
        context_instance=RequestContext(request))
    
