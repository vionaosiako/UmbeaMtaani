from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('registerPage', views.registerPage, name='registerPage'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('profilePage/<int:user_id>', views.profilePage, name='profilePage'),
    path('profileUpdates', views.profileUpdates, name='profileUpdates'),
    path('Neighbourhood', views.newHood, name='Neighbourhood'),
    path('hood', views.hood, name='hood'),
    path('business', views.business, name='business'),
]