from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreate, BlogList, BlogDetail, BlogUpdate

app_name = BlogConfig.name


urlpatterns = [
    path('blog/create/', BlogCreate.as_view(), name='blog_create'),
    path('blog/list/', BlogList.as_view(), name='blog_list'),
    path('blog/detail/<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path('blog/update/<int:pk>/', BlogUpdate.as_view(), name='blog_update'),
]
