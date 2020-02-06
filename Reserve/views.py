from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from Reserve.models import Roomtype
from django.template import context, loader
from django.contrib.auth import (authenticate,get_user_model,login,logout)
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
def index(request):

    return render(request,'showdata.html')

def signin(request):
    #rooms = Roomtype.objects.all()
    return render(request,'login_form.html')

def RoomType(request):
    rooms = Roomtype.objects.all()
    return render(request,'RoomType.html',{'rooms':rooms})

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=user,set_password=password)
            form.save()
            login(request,user)
        return redirect(request,'login_form.html')
    else:
        form=UserCreationForm()
        return render(request,'signup.html',{'form':form})

