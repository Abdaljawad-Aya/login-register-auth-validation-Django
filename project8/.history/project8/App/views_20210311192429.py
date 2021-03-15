from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return render(request , "index.html")

def registerPage(request):
    
    if request.method == 'POST' : 
    form = UserCreationForm()
    context ={'form':form}
    return render(request, '../templates/register.html', context)

def loginPage(request):
    context ={}
    return render(request, '../templates/login.html', context)