from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.edit import FormView
from .forms import ApplicationForm

def home(request):
    return render(request, 'main/home.html')

class ApplicationView(LoginRequiredMixin,FormView):
    template_name = 'main/application_form.html'
    form_class = ApplicationForm
    success_url = '/'

    def form_valid(self, form):
        form.applicant=self.request.user
        return super().form_valid(form)
