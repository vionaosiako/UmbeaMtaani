# Generated by Django 4.0.4 on 2022-06-18 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NeighbourhoodApp', '0007_remove_neighbourhood_admin_neighbourhood_area_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='occupants_count',
            new_name='population',
        ),
    ]
