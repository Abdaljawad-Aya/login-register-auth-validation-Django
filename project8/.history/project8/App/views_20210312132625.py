from django.shortcuts          import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib      import messages

from django.contrib.auth.decorators import login_required
# Create your views here.
from .models  import * 
from .forms   import OrderForm, CreateUserForm
from .filters import OrderFilters


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST': 
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account was updated ' + user)              

                    return redirect('login')
                  
    context ={'form':form}
    return render(request, '../templates/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
           return redirect('index')
    else:
           if request.method == 'POST':
                    username = request.POST.get('username')
                    password = request.POST.get('password')
                
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('index')
                    else: 
                        messages.info(request, 'Username OR password is incorrect')
                        # return render(request, '../templates/login.html', context)
            
    context ={'form':form}
    return render(request, '../templates/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# this is to make sure that the user is logged in first to be able to see the home page 
@login_required(login_url='login')
def index(request):
    return render(request , "index.html")
