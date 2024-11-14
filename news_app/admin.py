from django.contrib import admin
from .models import Category, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at',)
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    fields = ('title', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at',)
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    fields = ('image', 'title', 'content', 'category', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
