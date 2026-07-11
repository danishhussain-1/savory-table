"""
Views for the Gallery app.

Renders the public Gallery page with client-side-friendly category
filtering: all images and categories are passed to the template, and
JavaScript (static/js/menu-filter.js pattern, reused for gallery)
handles show/hide filtering without a page reload — matching the
smooth, app-like feel of the reference design.
"""
from django.shortcuts import render

from .models import GalleryCategory, GalleryImage


def gallery_view(request):
    """
    Renders the Gallery page with all categories and images.

    Filtering by category is done client-side via JavaScript for a
    snappy, no-reload experience (each image element carries a
    data-category attribute matching its category slug).
    """
    categories = GalleryCategory.objects.all()
    images = GalleryImage.objects.select_related('category').all()

    context = {
        'categories': categories,
        'images': images,
    }
    return render(request, 'gallery/gallery.html', context)