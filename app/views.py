"""
Definition of views.
"""

from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.core.exceptions import PermissionDenied

from datetime import datetime

# Database model definition
from . import models
from .forms import BootstrapAuthenticationForm

# Render index page
def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year': datetime.now().year,
        }
    )


@login_required
def edit_user(request, id):
    # get user object
    user = User.objects.get(id = id)

    # populate form input from query result
    user_form = BootstrapAuthenticationForm(request)




