#Create Models in this file.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='hadley_logo.png', blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, default = None)

    #Controls what the object displays when viewed in the shell using ClassName.objects.all()
    #Instead of returning the object, returns the title.
    def __str__(self):
        return self.title

    #returns first 50 characters of the article.
    #This works even though it says self.body is unsriptable.
    def snippet(self):
        return self.body[:50] + '...'