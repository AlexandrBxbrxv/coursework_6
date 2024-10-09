from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'views_count', 'is_published',)
    list_filter = ('owner', 'is_published',)
    search_fields = ('title',)
