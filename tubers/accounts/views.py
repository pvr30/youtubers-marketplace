from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from hiretubers.models import Hiretuber
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            return redirect('dashboard')
        else:
            messages.warning(request, 'invalid crendentials')
            return redirect('login')

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                    username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
        else:
            messages.warning(request, 'password do not match')
            return redirect('register')

    return render(request, 'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    hiretuber = Hiretuber.objects.all()
    data = {
        'hiretuber': hiretuber
    }
    return render(request, 'accounts/dashboard.html', data)
    