# Generated by Django 3.1.5 on 2021-01-10 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghar_dikhao', '0003_advertisment_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='category',
            field=models.CharField(choices=[('house', 'HOUSE'), ('banglow', 'BANGLOW'), ('apartment', 'APARTMENT')], default='house', max_length=10),
        ),
    ]
