from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        
        self.user = User(username='viona') 
        self.user.save()
        self.profile=Profile(user=self.user,fullname='viona',profile_pic='',email='viona@gmail.com',hood='Buruburu')
        
        
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
