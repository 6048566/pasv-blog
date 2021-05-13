from django.contrib import admin
from blog.models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_created', 'category']
    list_filter = ['time_created']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)