# Generated by Django 4.0.4 on 2022-06-19 19:55

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NeighbourhoodApp', '0009_remove_neighbourhood_population'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NeighbourhoodApp.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NeighbourhoodApp.profile')),
            ],
        ),
    ]
