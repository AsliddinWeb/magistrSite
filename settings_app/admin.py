from django.contrib import admin

from .models import SeoSettings, Navbar, SocialNetwork

class SeoSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_author', 'created_at', 'updated_at')

    search_fields = ('site_name', 'site_keywords', 'site_description')

    list_filter = ('created_at', 'updated_at')

    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('site_name', 'site_description', 'site_keywords', 'site_author')
        }),
        ('Rasm Sozlamalari', {
            'fields': ('site_logo', 'site_favicon', 'site_css')
        }),
        ('Vaqt Sozlamalari', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created_at', 'updated_at')

admin.site.register(SeoSettings, SeoSettingsAdmin)

@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'is_submenu', 'parent', 'created_at')
    list_filter = ('is_submenu', 'parent', 'created_at')
    search_fields = ('title', 'link')
    ordering = ('created_at',)
    list_editable = ('link', 'is_submenu', 'parent')
    fieldsets = (
        (None, {
            'fields': ('title', 'link', 'is_submenu', 'parent')
        }),
        ('Vaqt ma\'lumotlari', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'i_class')
    search_fields = ('title', 'link', 'i_class')
    list_editable = ('link', 'i_class')
    ordering = ('title',)