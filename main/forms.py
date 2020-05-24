from django import forms
from django.core.exceptions import ValidationError

from .models import Education
from datetime import date

accademic_level_choices = (
    ('year1', 'Year 1'),
    ('year2', 'Year 2'),
    ('year3', 'Year 3'),
    ('year4', 'Year 4'),
    ('year4', 'Year 5'),
)

class EducationForm(forms.Form):
    school_name=forms.CharField(max_length=30)
    school_address = forms.CharField(max_length=100)
    accademic_level = forms.CharField(widget=forms.Select(choices=accademic_level_choices))
    expected_completion_date = forms.DateField()

    def clean_expected_completion_date(self):
        expected_completion_date = self.cleaned_data['expected_completion_date']
        if expected_completion_date < date.today():
                raise ValidationError("Expected completion date must be a future date")
        return expected_completion_date

    class Meta:
        model=Education
        fields=['school_name','school_address','accademic_level','expected_completion_date']