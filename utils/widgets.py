import datetime
from django.forms import widgets

class SelectableTimeWidget(widgets.Select):
    """ Displays a list of hours. (24)

    """
    start_hour = None
    end_hour = None

    def __init__(self, start_hour=0, end_hour=24, *args, **kwargs):
        super(SelectableTimeWidget,self).__init__(*args, **kwargs)
        self.start_hour = start_hour
        self.end_hour = end_hour


    def render(self, name, value, attrs=None, choices=None):
        """Returns this Widget rendered as HTML, as a Unicode string."""
        if choices == None:
            choices = [(hour,str(hour).zfill(2) + 'h') for hour in\
              range(self.start_hour,self.end_hour)] 
        if isinstance(value, datetime.time):
            value = value.hour    
        return super(SelectableTimeWidget, self).render(name, value, attrs,
                choices)

