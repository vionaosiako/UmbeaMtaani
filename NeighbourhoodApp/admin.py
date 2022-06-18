from django.contrib import admin

# Register your models here.
from .models import Profile,Location
admin.site.register(Profile),
admin.site.register(Location)