# Generated by Django 3.1.5 on 2021-01-11 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ghar_dikhao', '0015_auto_20210111_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='user',
            field=models.ForeignKey(blank=True, default=5, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
