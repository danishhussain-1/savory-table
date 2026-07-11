"""
Views for the Core app: Home, About, Contact.

Keeping these thin and delegating data-fetching to each feature app's
models keeps the Core app focused purely on page composition.
"""
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from menu.models import MenuItem
from reviews.models import Review
from .forms import ContactForm, NewsletterForm
from .models import SiteStat


class HomeView(TemplateView):
    """
    Renders the home page: hero slider, special dishes, chef's story,
    site statistics, and a preview of the latest customer reviews.
    """
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_dishes'] = MenuItem.objects.filter(
            is_featured=True, is_available=True
        )[:4]
        context['site_stats'] = SiteStat.objects.all()
        context['latest_reviews'] = Review.objects.filter(
            is_approved=True
        ).select_related('user').order_by('-created_at')[:3]
        context['newsletter_form'] = NewsletterForm()
        return context


class AboutView(TemplateView):
    """Renders the About Us page with the restaurant's story and values."""
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsletter_form'] = NewsletterForm()
        return context


def contact_view(request):
    """
    Displays and processes the Contact Us form.

    On successful submission, saves the ContactMessage and shows a success
    message via Django's messages framework, then redirects (Post/Redirect/Get
    pattern) to avoid duplicate form submissions on page refresh.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for reaching out! We will get back to you shortly.'
            )
            return redirect('core:contact')
        else:
            messages.error(request, 'Please correct the errors below and try again.')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {
        'form': form,
        'newsletter_form': NewsletterForm(),
    })


def newsletter_signup_view(request):
    """
    Handles newsletter signup submissions from the footer form.

    This form appears on every page, so on success/failure we redirect back
    to whichever page the user submitted from (using the HTTP referer),
    falling back to the home page if unavailable.
    """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            from .models import NewsletterSubscriber
            _, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, 'You have been subscribed to our newsletter!')
            else:
                messages.info(request, 'You are already subscribed to our newsletter.')
        else:
            messages.error(request, 'Please enter a valid email address.')

    return redirect(request.META.get('HTTP_REFERER', 'core:home'))