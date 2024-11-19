from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import AddAnonMessageForm
from .models import AnonMessage

# Create your views here.
def add_anon_message(request,username):
    get_user = User.objects.get(username=username)
    if request.method == 'POST':
        form = AddAnonMessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.user = get_user
            msg.save()
            messages.success(request,f'Secret message has been sent to {get_user.first_name}')
            return redirect('dashboard:home')
        else:
            messages.warning(request,'Something went wrong.')
            return redirect('dashboard:add-anon-message')
    else:
        form = AddAnonMessageForm()
        return render(request,'dashboard/add-anon-message.html',{'form':form,'get_user':get_user})
    
def all_anon_messages(request):
    msgs = AnonMessage.objects.filter(user=request.user)
    return render(request,'dashboard/all-messages.html',{'msgs':msgs})

def home(request):
    return render(request,'dashboard/home.html')
