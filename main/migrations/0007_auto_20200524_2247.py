# Generated by Django 3.0.6 on 2020-05-24 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200524_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='accademic_level',
            field=models.CharField(choices=[('year1', 'Year 1'), ('year2', 'Year 2'), ('year3', 'Year 3'), ('year4', 'Year 4'), ('year4', 'Year 5')], default='year1', max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='expected_completion_date',
            field=models.DateTimeField(),
        ),
    ]
