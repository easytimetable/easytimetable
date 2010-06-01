import datetime
from django.forms import widgets

class SelectableTimeWidget(widgets.Select):
    """ Displays a list of hours. (24)

    """
    def render(self, name, value, attrs=None, choices=([('', ' -- ')] + 
        [(hour,str(hour).zfill(2) + 'h') for hour in range(0, 24)])):
        """Returns this Widget rendered as HTML, as a Unicode string."""
        if isinstance(value, datetime.time):
            value = value.hour    
        return super(SelectableTimeWidget, self).render(name, value, attrs,
                choices)

