from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration for the Accounts app.

    Handles user authentication (login/register/logout), user profiles,
    and the user-facing dashboard where customers can view their
    reservations and manage their account details.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = 'Accounts (Auth & Profiles)'

    def ready(self):
        """
        Import signal handlers when the app is ready.

        This connects the post_save signal on User that auto-creates a
        matching Profile object for every new user (see accounts/signals.py).
        """
        import accounts.signals  # noqa: F401