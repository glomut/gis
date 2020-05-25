from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

def register_applicant(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='applicant')
            user.groups.add(group)
            messages.success(request, f'Your account has been created. You are now able to login')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def register_sponsor(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='sponsor')
            user.groups.add(group)
            messages.success(request, f'Your account has been created. You are now able to login')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})
