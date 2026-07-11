from django.apps import AppConfig


class GalleryConfig(AppConfig):
    """
    Configuration for the Gallery app.

    Powers the restaurant's photo gallery page, showing categorized
    images of food, interior, and events, matching the reference design's
    "Gallery" page with All / Food / Interior / Events filter tabs.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gallery'
    verbose_name = 'Photo Gallery'