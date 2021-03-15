from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
from .models import * 
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilters


def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST': 
        form = CreateUserForm(request.POST)
        if form.is_valid():
              form.save()
              return redirect('login')
          
          
          
    context ={'form':form}
    return render(request, '../templates/register.html', context)


def loginPage(request):
    context ={}
    return render(request, '../templates/login.html', context)

def index(request):
    return render(request , "index.html")
