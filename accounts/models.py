"""
Models for the Accounts app.

Extends Django's built-in User model with a one-to-one Profile model,
rather than replacing the User model entirely. This is the recommended
approach for adding restaurant-specific fields (phone number, avatar,
bio) while keeping full compatibility with Django's built-in auth system.
"""
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Extra profile information attached to each Django User.

    A Profile is automatically created for every new User via a signal
    (see accounts/signals.py), so views can safely assume
    `request.user.profile` always exists for an authenticated user.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        help_text='Profile picture shown in the user dashboard.'
    )
    phone_number = models.CharField(max_length=20, blank=True)
    bio = models.TextField(
        max_length=300,
        blank=True,
        help_text='A short personal note (optional).'
    )
    address = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"{self.user.username}'s Profile"

    @property
    def full_name(self):
        """Convenience property: returns the user's full name, or username if blank."""
        full_name = f'{self.user.first_name} {self.user.last_name}'.strip()
        return full_name if full_name else self.user.username