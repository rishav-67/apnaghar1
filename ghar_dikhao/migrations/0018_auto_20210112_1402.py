# Generated by Django 3.1.5 on 2021-01-12 08:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ghar_dikhao', '0017_advertisment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
