# Generated by Django 3.0.8 on 2020-08-09 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
