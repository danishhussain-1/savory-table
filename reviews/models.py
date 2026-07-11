"""
Models for the Reviews app.

A single Review model serves two purposes depending on whether
`menu_item` is set:
- If `menu_item` is null: a general restaurant review (shown on the
  home page and the dedicated Reviews page).
- If `menu_item` is set: a review of that specific dish (shown on the
  menu item's detail page).

Reviews require admin approval (`is_approved`) before appearing
publicly, protecting the site from spam or inappropriate content.
"""
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from menu.models import MenuItem


class Review(models.Model):
    """A customer review with a 1–5 star rating."""

    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
        blank=True,
        help_text='Leave blank for a general restaurant review, or select a dish for a dish-specific review.'
    )
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    title = models.CharField(max_length=150, blank=True)
    comment = models.TextField()
    is_approved = models.BooleanField(
        default=False,
        help_text='Reviews are hidden from the public site until approved by an admin.'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        target = self.menu_item.name if self.menu_item else 'Savory Table (general)'
        return f'{self.rating}★ — {target} by {self.user.username}'