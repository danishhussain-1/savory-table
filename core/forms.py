"""
Forms for the Core app: Contact Us and Newsletter signup.
"""
from django import forms

from .models import ContactMessage, NewsletterSubscriber


class ContactForm(forms.ModelForm):
    """
    Public-facing contact form.

    Field widgets are styled with CSS classes matching the dark, elegant
    Savory Table theme (see static/css/about.css / base.css for styling).
    """

    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (234) 567-8900',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us how we can help...',
                'rows': 5,
            }),
        }

    def clean_full_name(self):
        """Ensure the name doesn't contain only whitespace."""
        full_name = self.cleaned_data['full_name'].strip()
        if not full_name:
            raise forms.ValidationError('Please enter your full name.')
        return full_name


class NewsletterForm(forms.ModelForm):
    """Compact single-field newsletter signup form used in the footer."""

    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'newsletter-input',
                'placeholder': 'Your Email',
            }),
        }

    def clean_email(self):
        """Normalize email to lowercase for consistent duplicate checks."""
        email = self.cleaned_data['email'].strip().lower()
        return email