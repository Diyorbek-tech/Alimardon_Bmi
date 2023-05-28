from django.urls import path
from .views import Homeview,Aboutview,Contactview
urlpatterns=[
    path('',Homeview.as_view(),name="home"),
    path('aboutus/',Aboutview.as_view(),name="aboutus"),
    path('contact/',Contactview.as_view(),name="contact"),

]