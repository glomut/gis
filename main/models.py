from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

accademic_level_choices = (
    ('year1', 'Year 1'),
    ('year2', 'Year 2'),
    ('year3', 'Year 3'),
    ('year4', 'Year 4'),
    ('year4', 'Year 5'),
)
class Application(models.Model):
    phone_number = PhoneNumberField()
    user_address=models.CharField(max_length=100)
    national_id=models.FileField(upload_to='documents/national_ids')
    birth_certificate=models.FileField(upload_to='documents/birth_certificates')
    school_name = models.CharField(max_length=100)
    school_address = models.CharField(max_length=100)
    accademic_level = models.CharField(max_length=10, choices=accademic_level_choices, default='year1')
    expected_completion_date = models.DateTimeField()
    moltivation = models.TextField(verbose_name='Why do you deserve sponsorship? ')
    recommendation_letter = models.FileField(upload_to='documents/recommendation_letters')
    status = models.CharField(max_length=30,default="pending")
    applicant = models.ForeignKey(User,related_name='applicant', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(default=timezone.now)
    approval_date = models.DateTimeField(default=None, blank=True, null=True)
    approved_by = models.ForeignKey(User,null=True, blank=True, related_name='approved_by', on_delete=models.SET_NULL)
    sponsor = models.ForeignKey(User, null=True, blank=True, related_name='sponsor', on_delete=models.SET_NULL)
    date_sponsored = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.school_name}, {self.school_address}'

    def get_absolute_url(self):
        return reverse('main-home')