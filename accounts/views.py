from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterUserForm

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Account created. Please log in.')
            return redirect('accounts:login')
        else:
            messages.warning(request,'Something went wrong.')
    else:
        form = RegisterUserForm()
    
    return render(request,'accounts/register.html',{'form':form})
    
def login_user(request):
    if request.method  == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None and user.is_active:
            login(request,user)
            return redirect('dashboard:home')
        else:
            messages.warning(request,'Something went wrong! Try again.')
    else:
        return render(request,'accounts/login.html')
    

def logout_user(request):
    logout(request)
    messages.info(request,'Session ended. Login to continue')
    return redirect('accounts:login')


