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

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('name', 'phone', 'message')
    list_editable = ('is_read',)
    ordering = ('-id',)


@admin.register(AboutWelcome)
class AboutWelcomeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'body')

@admin.register(AboutTeam)
class AboutTeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'cap_title', 'image')
    search_fields = ('title', 'cap_title', 'description')
    list_filter = ('title',)

@admin.register(AboutResult)
class AboutResultAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')

@admin.register(AboutAuthor)
class AboutAuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'phone', 'email')
    search_fields = ('title', 'address', 'phone', 'email')


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'correct_option', 'created_at', 'updated_at')
    list_filter = ('correct_option', 'created_at')
    search_fields = ('question', 'option_a', 'option_b', 'option_c', 'option_d')
