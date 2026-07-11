"""
Forms for the Reservations app.
"""
from django import forms
from django.utils import timezone

from .models import Reservation


class ReservationForm(forms.ModelForm):
    """
    Public "Book Your Table" form, matching the reference design's
    fields: Full Name, Phone Number, Email Address, Date, Time, Number
    of Guests, and Special Request.
    """

    class Meta:
        model = Reservation
        fields = [
            'full_name', 'email', 'phone_number',
            'reservation_date', 'reservation_time',
            'number_of_guests', 'special_request',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone',
            }),
            'reservation_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'reservation_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
            'number_of_guests': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'No. of Guests',
                'min': 1,
                'max': 20,
            }),
            'special_request': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Any special request...',
            }),
        }

    def clean_reservation_date(self):
        """Prevent bookings for dates in the past."""
        reservation_date = self.cleaned_data['reservation_date']
        if reservation_date < timezone.localdate():
            raise forms.ValidationError('Please select a date in the future.')
        return reservation_date

    def clean(self):
        """
        Cross-field validation: if the reservation is for today, the
        chosen time must not already be in the past.
        """
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get('reservation_date')
        reservation_time = cleaned_data.get('reservation_time')

        if reservation_date and reservation_time:
            now = timezone.localtime()
            if reservation_date == now.date() and reservation_time < now.time():
                raise forms.ValidationError(
                    'The selected time has already passed today. Please choose a later time.'
                )
        return cleaned_data