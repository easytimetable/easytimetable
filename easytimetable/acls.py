"""ACLs handlers for the application.

We define here who should have access to the resources. Each resource handler
takes two arguments: the action and the request, then determines if the user can
access the resource. 
"""
from functools import partial

def crud_acl_handler(resource):
    """Utility used to generate generic ACLs based on resources and profile.
    """
    return partial(_crud_acl, resource)

def _crud_acl(resource,request, action, can_view=True):
    if action in ('create', 'update', 'delete'):
        return _profile_based_acl(request, 'university') 
    elif action in ('view',):
        return can_view

def _profile_based_acl(request, resource):
    """A default profile based ACL ruler.
    """
    try:
        return getattr(request.user.get_profile(), 'can_manage_' + resource)()
    except:
        return False
