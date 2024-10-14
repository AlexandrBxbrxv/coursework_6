from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogCreate, BlogList, BlogDetail, BlogUpdate, BlogDelete

app_name = BlogConfig.name


urlpatterns = [
    path('blog/create/', BlogCreate.as_view(), name='blog_create'),
    path('blog/list/', BlogList.as_view(), name='blog_list'),
    path('blog/detail/<int:pk>/', cache_page(60)(BlogDetail.as_view()), name='blog_detail'),
    path('blog/update/<int:pk>/', BlogUpdate.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDelete.as_view(), name='blog_delete'),
]
