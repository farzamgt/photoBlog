from django.contrib import admin
from .models import Post, Category  

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    search_fields = ('title', 'content')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) 
