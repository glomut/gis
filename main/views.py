from datetime import date, datetime
from django.shortcuts import render
from.models import Education,Application
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.edit import FormView
from .forms import EducationForm

def home(request):
    return render(request, 'main/home.html')

class EducationView(LoginRequiredMixin,FormView):
    template_name = 'main/education_form.html'
    form_class = EducationForm
    success_url = '/'

    def form_valid(self, form):
        form.applicant=self.request.user
        return super().form_valid(form)



class ApplicationCreateView(LoginRequiredMixin,CreateView):
    model = Application
    fields=['defense','recommendation_letter']

    def form_valid(self, form):
        form.instance.applicant=self.request.user
        return super().form_valid(form)