# Generated by Django 3.1.5 on 2021-01-10 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ghar_dikhao', '0009_advertisment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='usercustom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=700)),
                ('first_name', models.CharField(max_length=700)),
                ('last_name', models.CharField(max_length=700)),
                ('link', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
