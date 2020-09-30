#Create Models in this file.

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='hadley_logo.png', blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, default = None)

    #Controls what the object displays when viewed in the shell using ClassName.objects.all()
    #Instead of returning the object, returns the title.
    def __str__(self):
        return self.title

    