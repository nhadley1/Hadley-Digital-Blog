#nate - This is the file where Models (Basically db tables) are stored


from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)