"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.core.mail import send_mail

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
        }
    )

def contact(request):
    """Renders the contact page."""
    #assert isinstance(request, HttpRequest)
    if request.method == "POST":
        company = request.POST.get('company')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        subject = name+(" From ")+company+(" wants to connect with EME Ready Mix")

        data = {
            'company': company,
            'name': name,
            'email': email,
            'phone': phone,
            'message': message,
            'subject': subject,
        }

        message = '''
        From: {} 

        Email: {}

        Company: {}

        Phone Number: {}

        {}
        '''.format(data['name'], data['email'], data['company'], data['phone'], data['message'])
        send_mail(data['subject'], message, '', ['magarciar931@gmail.com'])
    return render(
        request,
        'app/contact.html',
        {
            
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
        }
    )

def services(request):
    """Renders the services page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/services.html',
        {
        }
    )

def quickquote(request):
    """Renders the quotes page."""
    #assert isinstance(request, HttpRequest)
    if request.method == "POST":
        company = request.POST.get('company')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        projectdate = request.POST.get('projectdate')
        address = request.POST.get('address')
        message = request.POST.get('message')
        subject = name+(" From ")+company+(" Wants a Quote for a Project")

        data = {
            'company': company,
            'name': name,
            'email': email,
            'phone': phone,
            'projectdate': projectdate,
            'address': address,
            'message': message,
            'subject': subject,
        }

        message = '''
        From: {} 

        Email: {}

        Company: {}

        Phone Number: {}

        Project Date: {}

        Project Address: {}

        {}
        '''.format(data['name'], data['email'], data['company'], data['phone'], data['projectdate'], data['address'], data['message'])
        send_mail(data['subject'], message, '', ['magarciar931@gmail.com'])
    return render(
        request,
        'app/quickquote.html',
        {
        }
    )

def gallery(request):
    """Renders the galleries page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/gallery.html',
        {
        }
    )