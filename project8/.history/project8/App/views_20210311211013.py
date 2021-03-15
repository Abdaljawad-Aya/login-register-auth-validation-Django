from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter

def index(request):
    return render(request , "index.html")

def registerPage(request):
	# if request.user.is_authenticated:
	# 	return redirect('home')
	# else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
    
    context ={'form':form}
    return render(request, '../templates/register.html', context)


def loginPage(request):
    context ={}
    return render(request, '../templates/login.html', context)