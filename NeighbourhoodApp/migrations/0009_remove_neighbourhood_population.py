# Generated by Django 4.0.4 on 2022-06-19 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NeighbourhoodApp', '0008_rename_occupants_count_neighbourhood_population'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='population',
        ),
    ]