from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreate

app_name = BlogConfig.name


urlpatterns = [
    path('blog/create/', BlogCreate.as_view(), name='blog_create'),
]
