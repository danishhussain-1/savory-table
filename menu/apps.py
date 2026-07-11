from django.apps import AppConfig


class MenuConfig(AppConfig):
    """
    Configuration for the Menu app.

    Manages menu categories (Pizza, Burgers, Pasta, Steaks, Seafood,
    Desserts, Drinks) and individual menu items, and powers the public
    "Our Menu" page with search and category filtering.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
    verbose_name = 'Menu Management'