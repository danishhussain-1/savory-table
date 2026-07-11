"""
Views for the Reservations app.

Handles the public "Book a Table" form and the logged-in user's
"My Reservations" list (with the option to cancel an upcoming booking).
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReservationForm
from .models import Reservation


def reservation_create_view(request):
    """
    Displays and processes the public table reservation form.

    Works for both guest and logged-in users. If the user is
    authenticated, the reservation is automatically linked to their
    account and pre-fills name/email for convenience.
    """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if request.user.is_authenticated:
                reservation.user = request.user
            reservation.save()
            messages.success(
                request,
                'Your table has been requested! We will confirm your reservation shortly by email.'
            )
            return redirect('reservations:reservation_create')
        else:
            messages.error(request, 'Please correct the errors below and try again.')
    else:
        initial = {}
        if request.user.is_authenticated:
            initial = {
                'full_name': request.user.get_full_name() or request.user.username,
                'email': request.user.email,
                'phone_number': request.user.profile.phone_number,
            }
        form = ReservationForm(initial=initial)

    return render(request, 'reservations/reservation_form.html', {'form': form})


@login_required
def my_reservations_view(request):
    """
    Displays all reservations linked to the logged-in user's account,
    most recent first.
    """
    reservations = Reservation.objects.filter(user=request.user).order_by(
        '-reservation_date', '-reservation_time'
    )
    return render(request, 'reservations/my_reservations.html', {
        'reservations': reservations,
    })


@login_required
def cancel_reservation_view(request, pk):
    """
    Allows a user to cancel one of their own upcoming reservations.

    Restricted to the reservation's owner via get_object_or_404's user
    filter, so users cannot cancel someone else's booking by guessing
    an ID in the URL.
    """
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)

    if reservation.status in (Reservation.STATUS_PENDING, Reservation.STATUS_CONFIRMED):
        reservation.status = Reservation.STATUS_CANCELLED
        reservation.save(update_fields=['status', 'updated_at'])
        messages.success(request, 'Your reservation has been cancelled.')
    else:
        messages.warning(request, 'This reservation cannot be cancelled.')

    return redirect('reservations:my_reservations')