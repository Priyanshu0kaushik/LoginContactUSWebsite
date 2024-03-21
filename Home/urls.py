from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from Home import views   

admin.site.site_header = "Priyanshu's Website Portal"
admin.site.site_title= "Priyanshu's Website"
admin.site.index_title= "Priyanshu's Portal"

urlpatterns = [
    path('', views.home , name='Home'),
    path('about/',views.about, name='About'),
    path('login/',views.loginUser, name='login'),
    path('services/',views.services, name='services'),
    path('contact/',views.contact, name='Contact'),
    path('signup/',views.signup,name="signup"),
    path('myaccount/',views.myaccount,name="myaccount"),
    path('logout/',views.logoutUser,name="logout"),
]