"""
Models for the Reservations app.

A single Reservation model captures everything shown in the reference
design's "Book Your Table" form: full name, phone number, email, date,
time, number of guests, and an optional special request — plus a status
field so staff can track and manage bookings from the admin dashboard.
"""
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Reservation(models.Model):
    """A single table booking request."""

    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_CANCELLED = 'cancelled'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reservations',
        null=True,
        blank=True,
        help_text='Linked account if the guest was logged in when booking (optional for guest bookings).'
    )
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    number_of_guests = models.PositiveSmallIntegerField(
        default=2,
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )
    special_request = models.TextField(
        blank=True,
        help_text='Any dietary restrictions, seating preferences, or occasion notes.'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-reservation_date', '-reservation_time']
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return f'{self.full_name} — {self.reservation_date} at {self.reservation_time} ({self.get_status_display()})'

    @property
    def is_upcoming(self):
        """Convenience property used in templates to badge upcoming bookings."""
        return self.status in (self.STATUS_PENDING, self.STATUS_CONFIRMED)