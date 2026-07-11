from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    """
    Configuration for the Reviews app.

    Manages customer reviews and star ratings — both restaurant-wide
    reviews (shown on the home page / Reviews page) and dish-specific
    reviews (shown on individual menu item detail pages).
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'
    verbose_name = 'Reviews & Ratings'