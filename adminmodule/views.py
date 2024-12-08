from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
def projecthomepage(request):
    return render(request,'projecthomepage.html')

def librarianhomepage(request):
    return render(request,'librarianhomepage.html')

def librarypatronshomepage(request):
    return render(request,'librarypatronshomepage.html')

def signup(request):
    return render(request,'signup.html')

from django.contrib import messages
from django.contrib.auth.models import User,auth
def signup1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1 = request.POST['password']
        pass2= request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username is already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!')
                return render(request, 'projecthomepage.html')
        else:
            messages.info(request,'password does not match')
            return render(request,'signup.html')

def login(request):
    return render(request,'login.html')
def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1=request.POST['password']
        user = auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            if len(username)==10:
                return redirect('librarypatronshomepage')
            elif len(username)==5:
                return redirect('librarianhomepage')
            else:
                return redirect('projecthomepage')
        else:
            return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request,'projecthomepage.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def profilepage(request):
    return render(request, 'librarian/profile.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Update user's profile
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        return redirect('profilepage')  # Redirect to the profile page after updating

    return redirect('profilepage')  # Redirect to the profile page if not a POST request
