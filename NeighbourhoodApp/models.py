from django.db import models
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Profile(models.Model):
    profile_pic=CloudinaryField('image')
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=100,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.user.username
    
    @classmethod
    def search_profile(cls, fullname):
        return cls.objects.filter(user__username__icontains=fullname).all()
    
    @receiver(post_save,sender=User)
    def createUserProfile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
    @receiver(post_save,sender=User)
    def saveUserProfile(sender, instance, **kwargs):
        instance.profile.save()
    def saveProfile(self):
        self.user()

class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Neighbourhood(models.Model):
    image=CloudinaryField('image',null=True,blank=True)
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,default='Nairobi')
    population = models.IntegerField(default=0)
    police_contact=models.IntegerField(null=True,blank=True)
    hospital_contact=models.IntegerField(null=True,blank=True)
    area_admin = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def create_neigborhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_neighbourhood(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    # find neighbourhood by id
    @classmethod
    def find_neigborhood(cls, id):
        hood = cls.objects.get(id=id)
        return hood

    def __str__(self):
        return self.name