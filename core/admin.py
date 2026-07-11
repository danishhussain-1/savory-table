"""
Admin configuration for the Core app.

Registers ContactMessage, NewsletterSubscriber, and SiteStat with
customized list displays so the restaurant owner can manage them easily
from the Django admin dashboard.
"""
from django.contrib import admin

from .models import ContactMessage, NewsletterSubscriber, SiteStat


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('full_name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    list_editable = ('is_read',)
    ordering = ('-created_at',)

    fieldsets = (
        ('Sender Information', {
            'fields': ('full_name', 'email', 'phone_number')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'subscribed_at')
    list_filter = ('is_active', 'subscribed_at')
    search_fields = ('email',)
    list_editable = ('is_active',)
    ordering = ('-subscribed_at',)


@admin.register(SiteStat)
class SiteStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'display_order')
    list_editable = ('display_order',)
    ordering = ('display_order',)