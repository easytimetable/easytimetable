"""List of django views for plannings 
"""

def get_planning(request, what=None, extra_context={}):
    """Return the planning for `what`. What determines the method we will use.

    Special parameters can be set in `extra_parameters`.

    """

def add_event(request):
    pass

def update_event(request):
    """Add an avent for a class
    
    """

def add_course_event(request):
    pass

def update_course_event(request, class_event_id):
    pass

def delete_event(request, event_id):
    pass
