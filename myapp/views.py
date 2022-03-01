from django.shortcuts import redirect, render
from . models import user_register
from . forms import userform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def index(request):
    return render (request,'myapp/index.html')

def register(request):
    if request.method=='POST':
        fm=userform(request.POST)
        if fm.is_valid():
           username=request.POST['username']
           email=request.POST['email']
           password=request.POST['password']
           
           reg=user_register(username=username,email=email,password=password)
           reg.save()
           fm=userform()
    else:
        fm=userform()

    return render (request,'myapp/register.html',{'form':fm}) 
def signIn(request):
    
    if request.method == 'POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            peer=request.user
            user=authenticate(username=username,password=password)
            if user is not None:
                login( request,user)
                return redirect('/welcome')
            else:
                return redirect ('/login')    
    else:
        fm=AuthenticationForm()
    return render (request,'myapp/login.html',{'form': fm })    


def welcome(request):
    user=request.user
    return render(request,'myapp/welcome.html',{'user': user})    