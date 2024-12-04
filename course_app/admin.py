from django.contrib import admin
from .models import CourseCategory, Course

class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'cap_title', 'description', 'link', 'bg_color', 'image', 'file_image')
    search_fields = ('title', 'cap_title')
    list_filter = ('bg_color',)
    list_per_page = 20
    ordering = ('title',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description', 'link', 'created_at', 'updated_at')
    search_fields = ('title', 'category__title')
    list_filter = ('category', 'created_at')
    list_per_page = 20
    ordering = ('created_at',)

admin.site.register(CourseCategory, CourseCategoryAdmin)
admin.site.register(Course, CourseAdmin)
