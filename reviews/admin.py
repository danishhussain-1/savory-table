"""
Admin configuration for the Reviews app.

Lets admins approve/reject customer reviews before they appear
publicly, and filter/search through submissions.
"""
from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'menu_item', 'rating', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'rating', 'created_at')
    list_editable = ('is_approved',)
    search_fields = ('user__username', 'title', 'comment')
    ordering = ('-created_at',)
    autocomplete_fields = ['menu_item']

    fieldsets = (
        ('Reviewer & Target', {
            'fields': ('user', 'menu_item')
        }),
        ('Review Content', {
            'fields': ('rating', 'title', 'comment')
        }),
        ('Moderation', {
            'fields': ('is_approved', 'created_at')
        }),
    )
    readonly_fields = ('created_at',)

    actions = ['approve_reviews', 'unapprove_reviews']

    @admin.action(description='Approve selected reviews')
    def approve_reviews(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'{updated} review(s) approved.')

    @admin.action(description='Unapprove selected reviews')
    def unapprove_reviews(self, request, queryset):
        updated = queryset.update(is_approved=False)
        self.message_user(request, f'{updated} review(s) unapproved.')