# Generated by Django 3.0.6 on 2020-05-24 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200524_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date_sponsored',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
