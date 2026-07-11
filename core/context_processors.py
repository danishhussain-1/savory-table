"""
Custom context processors for the Core app.

Context processors inject variables into the context of EVERY template
rendered across the site, without needing to pass them manually in every
view. This is used here to expose site-wide branding information
(restaurant name, tagline, contact info, social links) to templates such
as the navbar and footer.
"""
from django.conf import settings


def site_settings(request):
    """
    Expose site-wide constants to all templates.

    Usage in templates:
        {{ site_name }}
        {{ site_tagline }}
        {{ site_phone }}
        {{ site_email }}
        {{ site_address }}
    """
    return {
        'site_name': getattr(settings, 'SITE_NAME', 'Savory Table'),
        'site_tagline': getattr(settings, 'SITE_TAGLINE', 'Fine Dining Restaurant'),
        'site_phone': '+1 234 567 8900',
        'site_email': 'info@savorytable.com',
        'site_address': '123 Foodie Street, New York, USA 10001',
        'site_hours': 'Mon – Sun: 10:00 AM – 11:00 PM',
        'social_links': {
            'facebook': 'https://facebook.com/savorytable',
            'instagram': 'https://instagram.com/savorytable',
            'twitter': 'https://twitter.com/savorytable',
            'pinterest': 'https://pinterest.com/savorytable',
        },
    }