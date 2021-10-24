from django.shortcuts import render, redirect
from .models import Slider, Team
from django.contrib import messages
"""
In django we can fetch the data from another app's model like we doing for Youtuber model 
and use it into webpages app.
"""
from youtubers.models import Youtuber

# for the contact page model come from hiretubers
from hiretubers.models import Contact

# Create your views here.


def home(request):
    slider = Slider.objects.all()
    teams = Team.objects.all()

    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)

    all_tubers = Youtuber.objects.order_by('-created_date')

    data = {
        'slider': slider,
        'teams': teams,
        'featured_youtubers':  featured_youtubers,
        'all_tubers': all_tubers
    }
    return render(request, 'webpages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'webpages/about.html', data)


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']
        
        contact = Contact(full_name=full_name, phone=phone, email=email,
                        company_name=company_name, subject=subject, message=message)

        contact.save()
        messages.success(request, 'Thanks for reaching out')
        return redirect('home')
        
    return render(request, 'webpages/contact.html')