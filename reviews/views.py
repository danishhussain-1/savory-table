"""
Views for the Reviews app.

Handles the public Reviews page (all approved general restaurant
reviews) and processing of new review submissions from both the
Reviews page and menu item detail pages.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from menu.models import MenuItem
from .forms import ReviewForm
from .models import Review


def review_list_view(request):
    """
    Renders the public Reviews page, showing all approved general
    restaurant reviews (menu_item is null) with pagination, plus a form
    for logged-in users to submit a new review.
    """
    reviews = Review.objects.filter(
        is_approved=True, menu_item__isnull=True
    ).select_related('user').order_by('-created_at')

    paginator = Paginator(reviews, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'review_form': ReviewForm() if request.user.is_authenticated else None,
    }
    return render(request, 'reviews/review_list.html', context)


@login_required
def submit_review_view(request):
    """
    Processes a general restaurant review submission from the Reviews
    page. Requires login so reviews can be attributed to a real account.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.menu_item = None
            review.save()
            messages.success(
                request,
                'Thank you for your review! It will appear once approved by our team.'
            )
        else:
            messages.error(request, 'Please correct the errors in your review and try again.')

    return redirect('reviews:review_list')


@login_required
def submit_menu_item_review_view(request, slug):
    """
    Processes a dish-specific review submission from a menu item's
    detail page.
    """
    item = get_object_or_404(MenuItem, slug=slug, is_available=True)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.menu_item = item
            review.save()
            messages.success(
                request,
                f'Thank you for reviewing {item.name}! Your review will appear once approved.'
            )
        else:
            messages.error(request, 'Please correct the errors in your review and try again.')

    return redirect('menu:menu_detail', slug=slug)