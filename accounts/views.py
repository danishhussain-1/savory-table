"""
Views for the Accounts app: registration, login, logout, profile, and
the user dashboard.
"""
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from reservations.models import Reservation
from reviews.models import Review
from .forms import RegisterForm, StyledLoginForm, ProfileUpdateForm, UserUpdateForm


class RegisterView(CreateView):
    """
    Handles new customer registration.

    On success, logs the newly created user in immediately (so they don't
    have to log in separately right after signing up) and redirects to
    their dashboard with a welcome message.
    """
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(
            self.request,
            f'Welcome to Savory Table, {self.object.first_name}! Your account has been created.'
        )
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


class StyledLoginView(LoginView):
    """Handles customer login using the dark-theme styled login form."""
    template_name = 'accounts/login.html'
    authentication_form = StyledLoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().first_name or form.get_user().username}!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)


class StyledLogoutView(LogoutView):
    """Handles customer logout and redirects to the home page."""
    next_page = reverse_lazy('core:home')


@login_required
def dashboard_view(request):
    """
    Renders the user dashboard: upcoming reservations, past reservations,
    and the user's submitted reviews, at a glance.
    """
    reservations = Reservation.objects.filter(user=request.user).order_by('-reservation_date', '-reservation_time')
    upcoming_reservations = reservations.filter(status__in=['pending', 'confirmed'])
    past_reservations = reservations.exclude(status__in=['pending', 'confirmed'])
    my_reviews = Review.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'upcoming_reservations': upcoming_reservations,
        'past_reservations': past_reservations,
        'my_reviews': my_reviews,
        'total_reservations': reservations.count(),
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
def profile_view(request):
    """
    Displays and processes the profile edit form, allowing the user to
    update both their core User fields (name, email) and their extended
    Profile fields (avatar, phone, bio, address) in a single submission.
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })