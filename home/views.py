from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import InternApplication
import random
import string

# Create your views here.

def home(request):
    return render(request, 'home.html')

def generate_random_string():
    return ''.join(random.choices(string.ascii_letters, k=3))

def generate_username(name):
    return name.replace(" ", "") + '_' +generate_random_string()

def generate_password(username):
    return username + '@'

def apply_for_internship(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desired_domain = request.POST.get('dd')
        email = request.POST.get('email')
        qualification = request.POST.get('Qualification')
        source = request.POST.get('us')
        phone = request.POST.get('phone')
        username = generate_username(name)
        password = generate_password(username)

        intern = InternApplication(
            name=name,
            desired_domain=desired_domain,
            email=email,
            qualification=qualification,
            source=source,
            phone=phone,
            username=username,
            password=password,
        )
        intern.save()

        # # Create a user instance
        # user = User.objects.create_user(
        # username=username,
        # password=password,
        # first_name = name.split()[0],
        # email=email
        # )

        # # Send email with username and password
        subject = 'Your Internship Account Details'
        message = render_to_string('email_template.html', {'username': username, 'password': password, 'name' : name})
        # send_mail(subject, message, 'no-reply@tradalab.tech', [email])

        print(name,desired_domain,email,qualification,source,phone,username,password)

        

        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})
