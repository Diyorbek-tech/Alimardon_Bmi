from django.db import models
from ckeditor.fields import RichTextField



class ModelCourse(models.Model):
    teacher = models.CharField(max_length=60)
    title = models.CharField(max_length=150)
    level = models.CharField(max_length=30)
    numlesson = models.IntegerField()
    image = models.CharField(max_length=255)
    status = models.CharField(default="New", max_length=10)
    createdc = models.DateTimeField(auto_now=True)
    updatedc = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:10]+"..."

class Lessons(models.Model):
    course=models.ForeignKey(ModelCourse,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    text = RichTextField()
    video_url=models.CharField(max_length=250)
    duration=models.IntegerField(help_text="min")

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name[:10]+"..."
