from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from.models import Biodata
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            messages.success(request, f'Your account has been created. You are now able to login')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})



class BiodataCreateView(LoginRequiredMixin,CreateView):
    model = Biodata
    fields=['phone_number','address','national_id','birth_certificate']

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)