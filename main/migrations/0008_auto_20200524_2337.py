# Generated by Django 3.0.6 on 2020-05-24 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200524_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Reject'), ('sponsored', 'Sponsor'), ('rejected', 'Reject')], default='pending', max_length=10),
        ),
    ]