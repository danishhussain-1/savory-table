"""
Forms for the Reviews app.
"""
from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Review submission form, used both for general restaurant reviews
    (Reviews page) and dish-specific reviews (menu item detail page).

    The `menu_item` field is deliberately excluded from the form itself;
    the view sets it explicitly based on context (None for a general
    review, or a specific MenuItem instance for a dish review) so users
    can never spoof which dish they're reviewing via form tampering.
    """

    class Meta:
        model = Review
        fields = ['rating', 'title', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Give your review a title (optional)',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Share your dining experience...',
            }),
        }

    def clean_comment(self):
        """Ensure the comment has meaningful content."""
        comment = self.cleaned_data['comment'].strip()
        if len(comment) < 10:
            raise forms.ValidationError('Please write a review of at least 10 characters.')
        return comment