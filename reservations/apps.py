from django.apps import AppConfig


class ReservationsConfig(AppConfig):
    """
    Configuration for the Reservations app.

    Powers the "Book a Table" flow: the public reservation form, storage
    of booking requests, status tracking (pending/confirmed/cancelled/
    completed), and the "My Reservations" view inside the user dashboard.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservations'
    verbose_name = 'Table Reservations'