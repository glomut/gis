# Generated by Django 3.0.6 on 2020-05-24 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200524_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('sponsored', 'Sponsored'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]