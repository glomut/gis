from django import forms
from django.core.exceptions import ValidationError

from .models import Application
from datetime import date

accademic_level_choices = (
    ('year1', 'Year 1'),
    ('year2', 'Year 2'),
    ('year3', 'Year 3'),
    ('year4', 'Year 4'),
    ('year4', 'Year 5'),
)

class ApplicationForm(forms.Form):
    user_address = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=100)
    school_name = forms.CharField(max_length=30)
    school_address = forms.CharField(max_length=100)
    national_id = forms.FileField()
    birth_certificate = forms.FileField()
    accademic_level = forms.CharField(widget=forms.Select(choices=accademic_level_choices))
    recommendation_letter = forms.FileField()
    moltivation=forms.CharField(widget=forms.Textarea)
    expected_completion_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    def clean_expected_completion_date(self):
        expected_completion_date = self.cleaned_data['expected_completion_date']
        if expected_completion_date < date.today():
            raise ValidationError("Expected completion date must be a future date")
        return expected_completion_date

    class Meta:
        model = Application
        fields = ['school_name', 'school_address', 'accademic_level', 'expected_completion_date','moltivation',
                  'recommendation_letter', 'phone_number','user_address','national_id','birth_certificate']
