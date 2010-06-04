from django.conf import settings

DEFAULT_LIST_TEMPLATE = getattr(settings, 'CRUD_DEFAULT_LIST_TEMPLATE', 
    'crud/list.html')
