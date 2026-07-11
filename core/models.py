"""
Models for the Core app.

Holds site-wide data that doesn't belong to a specific feature app:
- ContactMessage: messages submitted via the Contact page form
- NewsletterSubscriber: emails collected via the footer newsletter signup
- SiteStat: the "10+ Years Experience / 50+ Dishes / 15K+ Customers" style
  counters shown on the home page, editable from the admin dashboard.
"""
from django.db import models


class ContactMessage(models.Model):
    """Represents a message submitted through the public Contact Us form."""

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(
        default=False,
        help_text='Marked as read once an admin has reviewed this message.'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'{self.subject} — {self.full_name}'


class NewsletterSubscriber(models.Model):
    """Represents an email address subscribed to the restaurant newsletter."""

    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-subscribed_at']
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'

    def __str__(self):
        return self.email


class SiteStat(models.Model):
    """
    Represents a single statistic counter shown on the home page,
    e.g. "10+ Years of Experience", "15K+ Happy Customers".

    Making this a model (instead of hardcoding in the template) lets the
    restaurant owner update these numbers from the Django admin without
    touching any code.
    """
    label = models.CharField(
        max_length=100,
        help_text='e.g. "Years of Experience", "Happy Customers"'
    )
    value = models.CharField(
        max_length=20,
        help_text='e.g. "10+", "50+", "15K+", "20+"'
    )
    icon_class = models.CharField(
        max_length=50,
        blank=True,
        help_text='Optional icon identifier used by the template (e.g. an emoji or CSS class name).'
    )
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']
        verbose_name = 'Site Statistic'
        verbose_name_plural = 'Site Statistics'

    def __str__(self):
        return f'{self.value} {self.label}'