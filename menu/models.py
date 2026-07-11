"""
Models for the Menu app.

- Category: top-level menu groupings shown as filter tabs
  (e.g. "All", "Pizza", "Burgers", "Pasta", "Steaks", "Seafood",
  "Desserts", "Drinks") matching the reference UI design.
- MenuItem: an individual dish with price, image, rating, and
  availability, belonging to one Category.
"""
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """A menu category used to group and filter menu items."""

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Auto-generate the slug from the name if not explicitly set."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class MenuItem(models.Model):
    """An individual dish or drink offered on the menu."""

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='menu_items'
    )
    description = models.TextField(
        help_text='Short appetizing description shown on the menu detail page.'
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu/')
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=4.5,
        help_text='Average rating out of 5.0, e.g. 4.8'
    )
    is_featured = models.BooleanField(
        default=False,
        help_text='Featured dishes appear in the "Chef\'s Choice" section on the home page.'
    )
    is_available = models.BooleanField(
        default=True,
        help_text='Uncheck to temporarily hide this item from the public menu without deleting it.'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', 'name']
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Auto-generate a unique slug from the dish name if not set."""
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while MenuItem.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('menu:menu_detail', kwargs={'slug': self.slug})