from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from users.utils import searchProfile
from .forms import messageform, profileform



from django.contrib import messages

from .forms import CustomUserCreationForm

from .models import Message, Profile

def profiles(request):

    profiles, search_query= searchProfile(request)

    return render(request,'profiles.html',{'profiles':profiles, 'search_query': search_query})



def loginUser(request):

    if request.user.is_authenticated :
        return redirect('profiles')  

    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        

        # try:
        #     user= User.objects.get(username=username)
        # except:
        #     print('error')

        # try:
        #     user= authenticate(request, username=username, password=password)
        # except:
        #     messages.error(request, 'user dosnt exist')

        user= authenticate(request, username=username, password=password)



        if user is not None:
            login(request , user)
            messages.success(request, 'Logged in successsfuly')
            return redirect('account')
        else:
            messages.error(request, 'username or password is not incorrect')


    return render(request,'login-user.html',{})


def logoutUser(request): 
    logout(request) 
       
    return render(request,'login-user.html',{})



def registrationUser(request): 
    form= CustomUserCreationForm()

    if request.method == 'POST':
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            messages.success(request, 'user was created!')
            login(request, user)
            return redirect('account')

    return render(request,'registration-user.html',{'form': form})


def userProfile(request, pk): 
    profile= Profile.objects.get(id= pk)

    skills= profile.skill_set.all()
    projects= profile.project_set.all()
    return render(request,'user-profile.html',{'profile': profile , 'skills': skills, 'projects':projects})


def account(request): 
    profile= request.user.profile

    skills= profile.skill_set.all()
    projects= profile.project_set.all()
    return render(request,'account.html',{'profile': profile , 'skills': skills, 'projects':projects})


def editaccount(request):
    profile= request.user.profile
    form= profileform(instance=profile)

    if request.method == 'POST':
        form= profileform(request.POST, request.FILES , instance= profile)
        if form.is_valid():
            form.save()
            return redirect('account')
       
    return render(request,'editaccount.html',{'form':form})


def inbox(request):
    profile= request.user.profile
    messages= profile.messages.all()
    unread_count= messages.filter(is_read= False).count
       
    return render(request,'inbox.html',{'inbox_messages':messages, 'unread_count': unread_count})


def single_message(request, pk):
    profile= request.user.profile
    message= profile.messages.get(id=pk)
    if message.is_read== False :
        message.is_read = True
        message.save()
       
    return render(request,'single-message.html',{'single_message':message})


def create_message(request, pk):

    recipient= Profile.objects.get(id= pk)

    form= messageform()
    print('ok')
    

    if request.method == 'POST':
        form= messageform(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.sender= request.user.profile
            message.recipient= recipient
            message.save()
            return redirect('userProfile', pk= recipient.id )

       
    return render(request,'create-message.html',{'form':form})