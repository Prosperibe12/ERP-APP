from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
from django.conf import settings 
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
"""
All views for this webapp will be defined here
"""
# index view
def index_view(request):
    
    context = {
        'Title': 'Home Page | ERP'
    }
    return render(request, 'webapp/index.html', context)

# about page view
def about_page(request):
    
    context = {
        'Title': 'About Page'
    }
    return render(request, 'webapp/about.html', context)

# services page view
def services_page(request):
    
    context ={
        'Title': 'Services'
    }
    return render(request, 'webapp/services.html', context)

# contact page view
def contact_page(request):
    
    # process posted data
    if request.method == 'POST':
        name = request.POST.get('name')
        email =  request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contacts = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        if contacts:
            # prepare mail
            html_content = render_to_string('webapp/email.html', {
                'name': name
            })
            text_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, 'Message Sent Successfully!')
            return redirect('web:index') 
    
    context = {
        'Title': 'Contact Us'
    }
    return render(request, 'webapp/contact.html', context)

# appointment page view
def appointment_page(request):
    
    # process appointment here
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        date = request.POST.get('date')
        time = request.POST.get('time')
        
        appointment = Appointment.objects.create(name=name, email=email, message=message, date=date, time=time)
        
        if appointment:
            html_content = render_to_string('webapp/email.html', {
                'name':name
            })
            text_content = strip_tags(html_content)
            msg = EmailMultiAlternatives('APPOINTMENT SCHEDULE', text_content, settings.EMAIL_HOST_USER, [email])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
            messages.success(request, 'Message sent Successfully.')
            return redirect('web:index')
    context = {
        'Title': 'Appointment Page',
        'name': 'appointment'
    }
    return render(request, 'webapp/appointment.html', context)

# career page view
def career_page(request):
    
    context = {
        'Title': 'Careers'
    }
    return render(request, 'webapp/careers.html', context)
