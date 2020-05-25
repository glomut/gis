from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from.models import Application
from django.views import generic
from django.views.generic import DetailView,UpdateView,ListView
from bootstrap_datepicker_plus import DateTimePickerInput
from django.core.mail import send_mail,EmailMessage
from sponsorship.settings import EMAIL_HOST_USER

def home(request):
    if request.user.is_authenticated:
        for group in request.user.groups.all():
            if str(group) =="applicant":
                app=Application.objects.all().filter(applicant=request.user).first()
                print(app)
                if app:
                    return redirect(app)
                return redirect('application-create')
            elif str(group) == "sponsor" or str(group) == "staff":
                return redirect('main-applications')
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

class ApplicationDetailView(UserPassesTestMixin,DetailView):
    model=Application

    def test_func(self):
        application=self.get_object()
        if self.request.user==application.applicant:
            return True
        else:
            for group in self.request.user.groups.all():
                print(group)
                if str(group) in ["staff","sponsor"]:
                    return True
            return False

# change view so that sponsors see only approved application
class ApplicationUpdateView(LoginRequiredMixin,UpdateView):
    model = Application
    template_name = 'main/application_detail.html'
    fields=['status']

    def send_approval_email(self, reciever,status):
        subject = 'Sponsorship Application Update'
        message = 'Your application for sponsorship  has been '+ str(status).upper()
        send_mail(subject, message, EMAIL_HOST_USER, [reciever])

    def send_sponsor_email(self, reciever,status, sponsor):
        subject = 'Sponsorship Application Update'
        message = 'Congratulations! You have recieved sponsorship. Your Sponsor is '+ \
                  sponsor[0].capitalize()  +" "+ sponsor[1].capitalize()  +"\n" +'Email address: '+ sponsor[2]
        send_mail(subject, message, EMAIL_HOST_USER, [reciever])

    def form_valid(self, form):
        if str(form.instance.status)=='sponsored':
            self.sponsor=[self.request.user.first_name, self.request.user.last_name, self.request.user.email]
            self.send_sponsor_email(form.instance.applicant.email,form.instance.status, self.sponsor)
        else:
            self.send_approval_email(form.instance.applicant.email, form.instance.status)
        form.instance.approved_by=self.request.user
        form.instance.approval_date = datetime.now()
        return super().form_valid(form)

    def test_func(self):
        for group in self.request.user.groups.all():
            print(group)
            if str(group) == "staff":
                return True
        return False



class ApplicationListView(ListView):
    model=Application
    template_name = 'main/applications.html'
    context_object_name = 'applications'
    ordering=['-submission_date',]

    # fix
    def test_func(self):
        for group in self.request.user.groups.all():
            print(group)
            if str(group) == "staff":
                return True
        return False