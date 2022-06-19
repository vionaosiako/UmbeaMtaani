from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import  CreateUserForm,NeighbourhoodForm
from .models import Profile,Location,Neighbourhood
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def registerPage(request):
    form =  CreateUserForm()
    contex = {'form':form}
    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # messages.success(request, 'Account was created for ' + user)
            return redirect('loginPage')
    return render(request, 'auth/register.html', contex)

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')
    contex = {}
    return render(request, 'auth/login.html', contex)
def logoutUser(request):
	logout(request)
	return redirect('loginPage')

# Create your views here.
def index(request):
    locations=Location.objects.all()
    hoods=Neighbourhood.objects.all()
    contex={'locations':locations, 'hoods':hoods}
    return render(request, 'index.html',contex)

@login_required(login_url='loginPage')
def profilePage(request,user_id):
    locations=Location.objects.all()
    profile=Profile.objects.get(id=user_id)
    contex = {'profile':profile,'locations':locations}
    return render(request, 'profile.html', contex)

# @login_required(login_url='loginPage')
# def location(request):
#     if request.method == 'POST':
#         locationform = LocationForm(request.POST,request.FILES)
#         if  locationform.is_valid:
#             locationform.save()
#             return redirect('index')
#     else:
#         locationform=LocationForm()
#     return render(request,'location.html',{'form':locationform})

@login_required(login_url='loginPage')
def newHood(request):
    locations=Location.objects.all()
    user = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form=NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.profile = user
            data.user=request.user.profile
            data.save()
            return redirect('index')
        else:
            form=ProjectForm()

    return render(request, 'AddNeighbourhood.html',{'form':NeighbourhoodForm, 'locations':locations})