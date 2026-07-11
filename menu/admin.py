"""
Admin configuration for the Menu app.

Lets the restaurant owner manage categories and menu items, including
availability toggles and featured-dish selection, directly from the
Django admin dashboard.
"""
from django.contrib import admin

from .models import Category, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'display_order')
    list_editable = ('display_order',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('display_order', 'name')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'rating', 'is_featured', 'is_available')
    list_filter = ('category', 'is_featured', 'is_available')
    list_editable = ('is_featured', 'is_available')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-is_featured', 'name')

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Pricing & Rating', {
            'fields': ('price', 'rating')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Visibility', {
            'fields': ('is_featured', 'is_available')
        }),
    )