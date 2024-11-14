from django.contrib import admin
from .models import *

@admin.register(HomeWelcome)
class HomeWelcomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'stat_title', 'image')
    search_fields = ('title', 'stat_title')
    list_filter = ('title',)
    fieldsets = (
        (None, {
            'fields': ('image', 'stat_title', 'stat_text', 'title', 'body')
        }),
    )

@admin.register(HomeWelcomeButton)
class HomeWelcomeButtonAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'css_class')
    search_fields = ('title', 'link')
    list_filter = ('css_class',)
    fieldsets = (
        (None, {
            'fields': ('title', 'link', 'css_class')
        }),
    )

@admin.register(CourseRightButton)
class CourseRightButtonAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'css_class')
    search_fields = ('title', 'link')
    ordering = ('title',)

    fieldsets = (
        (None, {
            'fields': ('title', 'link', 'css_class')
        }),
    )