# Generated by Django 4.0.4 on 2022-06-18 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NeighbourhoodApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone_number',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
