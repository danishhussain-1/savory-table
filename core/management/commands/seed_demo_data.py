"""
Management command: seed_demo_data

Populates the database with realistic demo/sample data so the site looks
fully populated immediately — useful for portfolio demos and local testing
without manually creating dozens of records in the Django admin.

Usage:
    python manage.py seed_demo_data

Safe to re-run: uses get_or_create() everywhere, so running it multiple
times won't create duplicate records.
"""
from django.core.management.base import BaseCommand

from core.models import SiteStat
from gallery.models import GalleryCategory
from menu.models import Category


class Command(BaseCommand):
    help = 'Seeds the database with demo categories and site statistics (menu item images must be added manually via admin).'

    def handle(self, *args, **options):
        self.stdout.write('Seeding demo data for Savory Table...')

        # ---- Menu Categories ----
        menu_categories = [
            ('Pizza', 1), ('Burgers', 2), ('Pasta', 3),
            ('Steaks', 4), ('Seafood', 5), ('Desserts', 6), ('Drinks', 7),
        ]
        for name, order in menu_categories:
            obj, created = Category.objects.get_or_create(
                name=name, defaults={'display_order': order}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  Created menu category: {name}'))

        # ---- Gallery Categories ----
        gallery_categories = [('Food', 1), ('Interior', 2), ('Events', 3)]
        for name, order in gallery_categories:
            obj, created = GalleryCategory.objects.get_or_create(
                name=name, defaults={'display_order': order}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  Created gallery category: {name}'))

        # ---- Site Stats ----
        site_stats = [
            ('Years of Experience', '10+', 1),
            ('Delicious Dishes', '50+', 2),
            ('Happy Customers', '15K+', 3),
            ('Awards Won', '20+', 4),
        ]
        for label, value, order in site_stats:
            obj, created = SiteStat.objects.get_or_create(
                label=label, defaults={'value': value, 'display_order': order}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  Created site stat: {value} {label}'))

        self.stdout.write(self.style.SUCCESS(
            '\nDone! Categories and stats are seeded. '
            'Please add Menu Items and Gallery Images manually via /admin/ (they require image uploads).'
        ))