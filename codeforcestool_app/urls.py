from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('ourteam/',views.ourteam,name='ourteam'),
    path('contactus/',views.contactus,name='contactus'),
    path('register',views.register,name='register'),
    path('iccc2020/',views.iccc2020,name='iccc2020'),
]
