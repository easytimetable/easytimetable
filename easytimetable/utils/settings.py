"""Settings for the crud utils.

"""
from django.conf import settings

DEFAULT_LIST_TEMPLATE = getattr(settings, 'CRUD_DEFAULT_LIST_TEMPLATE', 
    'crud/list.html')
DEFAULT_RESOURCE_ACCESS = getattr(settings,
    'CRUD_DEFAULT_RESOURCE_ACCESS', True)

# Default callable returns always True
DEFAULT_ACL_HANDLER= lambda request, right, *args, **kwargs: DEFAULT_RESOURCE_ACCESS
