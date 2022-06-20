# Generated by Django 4.0.4 on 2022-06-20 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NeighbourhoodApp', '0014_remove_neighbourhood_user_profile_hood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbor', to='NeighbourhoodApp.neighbourhood'),
        ),
    ]
