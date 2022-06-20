# Generated by Django 4.0.4 on 2022-06-20 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NeighbourhoodApp', '0015_alter_profile_hood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='hood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='NeighbourhoodApp.neighbourhood'),
        ),
        migrations.AlterField(
            model_name='post',
            name='hood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='NeighbourhoodApp.neighbourhood'),
        ),
    ]
