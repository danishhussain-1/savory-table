"""
Signal handlers for the Accounts app.

Automatically creates (and saves) a Profile instance whenever a new User
is created, so every user always has an associated profile without any
manual setup required elsewhere in the codebase.
"""
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create a Profile the first time a User is created.

    On subsequent saves of an existing User (created=False), this simply
    ensures the related Profile is saved too, guarding against edge cases
    where a Profile might be missing (e.g. for superusers created via
    `createsuperuser` before this signal existed).
    """
    if created:
        Profile.objects.create(user=instance)
    else:
        # Ensure a profile exists even for pre-existing users (defensive).
        Profile.objects.get_or_create(user=instance)