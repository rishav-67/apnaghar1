# Generated by Django 3.1.5 on 2021-01-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghar_dikhao', '0019_advertisment_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
