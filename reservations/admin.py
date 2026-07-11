"""
Admin configuration for the Reservations app.

Lets restaurant staff view, filter, and update the status of incoming
table reservation requests from the Django admin dashboard.
"""
from django.contrib import admin

from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'reservation_date', 'reservation_time',
        'number_of_guests', 'status', 'created_at',
    )
    list_filter = ('status', 'reservation_date')
    list_editable = ('status',)
    search_fields = ('full_name', 'email', 'phone_number')
    date_hierarchy = 'reservation_date'
    ordering = ('-reservation_date', '-reservation_time')

    fieldsets = (
        ('Guest Information', {
            'fields': ('user', 'full_name', 'email', 'phone_number')
        }),
        ('Booking Details', {
            'fields': ('reservation_date', 'reservation_time', 'number_of_guests', 'special_request')
        }),
        ('Status', {
            'fields': ('status', 'created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

    actions = ['mark_confirmed', 'mark_completed', 'mark_cancelled']

    @admin.action(description='Mark selected reservations as Confirmed')
    def mark_confirmed(self, request, queryset):
        updated = queryset.update(status=Reservation.STATUS_CONFIRMED)
        self.message_user(request, f'{updated} reservation(s) confirmed.')

    @admin.action(description='Mark selected reservations as Completed')
    def mark_completed(self, request, queryset):
        updated = queryset.update(status=Reservation.STATUS_COMPLETED)
        self.message_user(request, f'{updated} reservation(s) marked completed.')

    @admin.action(description='Mark selected reservations as Cancelled')
    def mark_cancelled(self, request, queryset):
        updated = queryset.update(status=Reservation.STATUS_CANCELLED)
        self.message_user(request, f'{updated} reservation(s) cancelled.')