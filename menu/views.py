"""
Views for the Menu app: menu listing (with search + category filter +
pagination) and menu item detail pages.
"""
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from reviews.forms import ReviewForm
from reviews.models import Review
from .models import Category, MenuItem


def menu_list_view(request):
    """
    Renders the public "Our Menu" page.

    Supports:
    - Category filtering via ?category=<slug> (defaults to "All")
    - Free-text search via ?q=<term> across dish name and description
    - Pagination (8 items per page, matching the reference design's 4x2 grid)
    """
    categories = Category.objects.all()
    items = MenuItem.objects.filter(is_available=True).select_related('category')

    selected_category = request.GET.get('category', '')
    if selected_category:
        items = items.filter(category__slug=selected_category)

    query = request.GET.get('q', '').strip()
    if query:
        items = items.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    paginator = Paginator(items, 8)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'page_obj': page_obj,
        'selected_category': selected_category,
        'query': query,
    }
    return render(request, 'menu/menu_list.html', context)


def menu_detail_view(request, slug):
    """
    Renders a single menu item's detail page, along with approved
    customer reviews for that dish and a form to submit a new review
    (handled by the reviews app's own POST endpoint).
    """
    item = get_object_or_404(MenuItem, slug=slug, is_available=True)
    related_items = MenuItem.objects.filter(
        category=item.category, is_available=True
    ).exclude(pk=item.pk)[:4]
    reviews = Review.objects.filter(
        menu_item=item, is_approved=True
    ).select_related('user').order_by('-created_at')

    context = {
        'item': item,
        'related_items': related_items,
        'reviews': reviews,
        'review_form': ReviewForm(),
    }
    return render(request, 'menu/menu_detail.html', context)