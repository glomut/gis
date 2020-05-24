from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.exceptions import ValidationError
from.models import Application
from django.views import generic
from bootstrap_datepicker_plus import DateTimePickerInput

def home(request):
    if request.user.is_authenticated:
        for group in request.user.groups.all():
            if str(group) =="applicant":
                return redirect('application-create')
            elif str(group) == "sponsor":
                return redirect('main-home')
    return render(request, 'main/home.html')

class ApplicationCreateView(LoginRequiredMixin,generic.edit.CreateView):
    model = Application

    fields = ['school_name', 'school_address', 'accademic_level', 'expected_completion_date', 'moltivation',
             'recommendation_letter', 'phone_number', 'user_address', 'national_id', 'birth_certificate']

    def get_form(self):
        form = super().get_form()
        form.fields['expected_completion_date'].widget = DateTimePickerInput()
        return form

    def form_valid(self, form):
        form.instance.applicant=self.request.user
        return super().form_valid(form)

    def clean_expected_completion_date(self):
        expected_completion_date = self.cleaned_data['expected_completion_date']
        if expected_completion_date < datetime.now():
            raise ValidationError("Expected completion date must be a future date")
        return expected_completion_date
