from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Configuration for the Core app.

    The Core app handles the site-wide public pages: Home, About, Contact,
    and Newsletter signup — the parts of the site that aren't tied to a
    specific domain model like menu items or reservations.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Core (Home / About / Contact)'