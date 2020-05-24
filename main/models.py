from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Education(models.Model):
    school_name = models.CharField(max_length=100)
    school_address = models.CharField(max_length=100)
    accademic_level = models.CharField(max_length=10, default='year1')
    expected_completion_date = models.DateField()
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school_name}, {self.school_address}, {self.accademic_level},' \
               f'{self.expected_completion_date}'

    def get_absolute_url(self):
        return reverse('main-home')


class Application(models.Model):
    defense = models.TextField(verbose_name='Why do you deserve sponsorship? ')
    recommendation_letter = models.FileField(upload_to='documents/recommendation_letters')
    status = models.CharField(max_length=30,default="pending")
    applicant = models.ForeignKey(User,related_name='applicant', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(default=timezone.now)
    approval_date = models.DateTimeField(null=True)
    approved_by = models.ForeignKey(User,null=True, related_name='approved_by', on_delete=models.SET_NULL)

    def __str__(self):
        return self.defense

    def get_absolute_url(self):
        return reverse('main-home')