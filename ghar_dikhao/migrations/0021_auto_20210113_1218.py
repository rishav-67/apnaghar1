# Generated by Django 3.1.5 on 2021-01-13 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghar_dikhao', '0020_auto_20210112_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisment',
            name='balcony',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='no', max_length=10),
        ),
        migrations.AddField(
            model_name='advertisment',
            name='bathroom',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisment',
            name='bedroom',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisment',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisment',
            name='district',
            field=models.CharField(default='dhanbad', max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisment',
            name='state',
            field=models.CharField(default='jharkhand', max_length=70),
            preserve_default=False,
        ),
    ]
