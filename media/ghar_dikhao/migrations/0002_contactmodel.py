# Generated by Django 3.1.5 on 2021-01-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghar_dikhao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.TextField(max_length=10)),
                ('subject', models.TextField(max_length=500)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]
