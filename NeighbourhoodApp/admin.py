from django.contrib import admin

# Register your models here.
from .models import Profile,Location,Neighbourhood
admin.site.register(Profile),
admin.site.register(Location),
admin.site.register(Neighbourhood)