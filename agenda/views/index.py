# django imports
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

# app import
from agenda.views import render_to_response
#from agenda.models import 
#from agenda.forms import

def index(request):
    return render_to_response('agenda/index.html', {}, request)
