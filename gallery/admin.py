"""
Admin configuration for the Gallery app.

Lets the restaurant owner upload and organize gallery photos by
category directly from the Django admin dashboard.
"""
from django.contrib import admin

from .models import GalleryCategory, GalleryImage


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'display_order')
    list_editable = ('display_order',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('display_order', 'name')


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'display_order', 'uploaded_at')
    list_filter = ('category', 'is_featured')
    list_editable = ('is_featured', 'display_order')
    search_fields = ('title',)
    ordering = ('display_order', '-uploaded_at')