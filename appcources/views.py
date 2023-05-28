from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
# Create your views here.
from .models import ModelCourse,Lessons

def courcesview(request):
    context={
        "courses_list":ModelCourse.objects.all()
    }
    return render(request,template_name='course.html',context=context)


def lessonview(request,pk):
    context = {
        "id":pk,
        "lesson_list": Lessons.objects.filter(course=pk)
    }
    return render(request, template_name='category.html', context=context)

def lessondetailsview(request,pk,pk2):
    context = {
        "lessondetails_list": Lessons.objects.filter(course=pk).get(id=pk2)
    }
    return render(request, template_name='event_details.html', context=context)


