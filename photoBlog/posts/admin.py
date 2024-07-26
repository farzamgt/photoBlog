from django.contrib import admin
from .models import Post, Category 
from django.utils.html import format_html


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    search_fields = ('title', 'content')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    fields = ('name', 'image')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50"/>'.format(obj.image.url))
        return None

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True