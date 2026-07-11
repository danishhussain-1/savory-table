"""
Models for the Gallery app.

- GalleryCategory: filter tabs shown on the Gallery page
  (e.g. "Food", "Interior", "Events"), matching the reference UI.
- GalleryImage: a single photo belonging to one category, with an
  optional caption and a flag to control display order/highlighting.
"""
from django.db import models
from django.utils.text import slugify


class GalleryCategory(models.Model):
    """A category used to filter gallery images (e.g. Food, Interior, Events)."""

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = 'Gallery Category'
        verbose_name_plural = 'Gallery Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Auto-generate the slug from the name if not explicitly set."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class GalleryImage(models.Model):
    """A single photo displayed in the restaurant's photo gallery."""

    category = models.ForeignKey(
        GalleryCategory,
        on_delete=models.CASCADE,
        related_name='images'
    )
    title = models.CharField(
        max_length=150,
        blank=True,
        help_text='Optional short caption shown on hover/lightbox.'
    )
    image = models.ImageField(upload_to='gallery/')
    is_featured = models.BooleanField(
        default=False,
        help_text='Featured images can be highlighted with larger display in the grid.'
    )
    display_order = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', '-uploaded_at']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title if self.title else f'{self.category.name} photo #{self.pk}'