from django.urls import path
from .views import courcesview,lessonview,lessondetailsview
urlpatterns=[
    path('',courcesview,name="courses"),
    path('<int:pk>/lessons/',lessonview,name="details"),
    path('<int:pk>/lessons/<int:pk2>',lessondetailsview,name="details_les"),

]