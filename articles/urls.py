
from django.urls import path
from . import views

#namespaces so if there are other apps with 
#paths with the same name we will be taken to the correct url.
app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name = "list"),
    path('create/', views.article_create, name= "create"),
    path('<slug>/', views.article_detail, name = "detail")
]



