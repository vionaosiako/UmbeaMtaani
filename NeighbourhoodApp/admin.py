from django.contrib import admin

# Register your models here.
from .models import Profile,Location,Neighbourhood,Business,Post
admin.site.register(Profile),
admin.site.register(Location),
admin.site.register(Neighbourhood),
admin.site.register(Business),
admin.site.register(Post),