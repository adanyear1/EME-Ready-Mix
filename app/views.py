"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact Us',
            'message':'We Are Happy To Connect With You!',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def services(request):
    """Renders the services page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/services.html',
        {
            'title':'Our Services',
            'year':datetime.now().year,
        }
    )

def quickquote(request):
    """Renders the quotes page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/quickquote.html',
        {
            'title':'Recieve A Fast Quote ',
            'message':'Tell us about your load and other requirements and we’ll provide a quick quote. You can also call us at 512-000-0000 or email us at sales@transco.com.',
            'year':datetime.now().year,
        }
    )

def gallery(request):
    """Renders the galleries page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/gallery.html',
        {
            'title':'Check Out Our Work ',
            'year':datetime.now().year,
        }
    )