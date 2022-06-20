from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import  CreateUserForm,NeighbourhoodForm,ProfileForm,BusinessForm,PostForm
from .models import Profile,Location,Neighbourhood,Business,Post
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

@login_required(login_url='loginPage')
def profileUpdates(request):
    current_user=request.user
    profile = Profile.objects.filter(id=current_user.id).first()
    locations=Location.objects.all()
    if request.method == 'POST':
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)
        if  profileform.is_valid:
            profileform.save(commit=False)
            profileform.user=request.user
            profileform.save()
            return redirect('index')
    else:
        form=ProfileForm(instance=profile)
    return render(request,'addProfile.html',{'form':form, 'locations':locations})

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

# def hood(request):
#     locations=Location.objects.all()
#     # neighborhoods = Neighbourhood.objects.get(id=neighborhood_id)
#     contex={'locations':locations}
#     return render(request, 'hood.html',contex)

def join_hood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.hood = neighbourhood
    request.user.profile.save()
    return redirect('index')

def leave_hood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.hood = None
    request.user.profile.save()
    return redirect('index')

def business(request):
    locations=Location.objects.all()
    user = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form=BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.profile = user
            data.user=request.user.profile
            data.save()
            return redirect('index')
        else:
            form=BusinessForm()
    contex={'locations':locations,'form':BusinessForm,}
    return render(request, 'addBusiness.html',contex)

@login_required(login_url='loginPage')
def newPost(request):
    locations=Location.objects.all()
    user = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.profile = user
            data.user=request.user.profile
            data.save()
            return redirect('index')
        else:
            form=PostForm()

    return render(request, 'addPost.html',{'locations':locations,'form':PostForm})
