# Generated by Django 3.1.5 on 2021-01-11 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghar_dikhao', '0012_extenduser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extenduser',
            old_name='first_name',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='extenduser',
            old_name='last_name',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='extenduser',
            name='email',
        ),
    ]
