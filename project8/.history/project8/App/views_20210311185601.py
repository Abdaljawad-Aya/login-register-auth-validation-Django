from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , "index.html")

def registerPage(request):
    context ={}
    return render(request, '../templates/register.html', context)

def loginPage(request):
    context ={}
    return render(request, '../templates/login.html', context)