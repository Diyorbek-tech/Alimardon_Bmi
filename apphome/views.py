from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
# Create your views here.


class Homeview(TemplateView):
    template_name = 'base.html'

class Aboutview(TemplateView):
    template_name = 'about.html'

class Contactview(TemplateView):
    template_name = 'contact.html'