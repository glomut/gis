from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

class Biodata(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = PhoneNumberField(blank=True)
    address=models.CharField(max_length=100)
    national_id=models.FileField(upload_to='documents/national_ids')
    birth_certificate=models.FileField(upload_to='documents/birth_certificates')

    def __string__(self):
        return f'{self.user.first_name} Profile'

    def get_absolute_url(self):
        return reverse('main-home')