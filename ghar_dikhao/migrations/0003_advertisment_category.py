# Generated by Django 3.1.4 on 2021-01-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghar_dikhao', '0002_contactmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisment',
            name='category',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=7),
        ),
    ]
