# bookings/forms.py

from django import forms
from .models import Booking

BUDGET_CHOICES = [
    ('', 'Select budget range'),
    ('under_100k', 'Under ₦100,000'),
    ('100k_300k', '₦100,000 – ₦300,000'),
    ('300k_600k', '₦300,000 – ₦600,000'),
    ('600k_1m', '₦600,000 – ₦1,000,000'),
    ('above_1m', 'Above ₦1,000,000'),
]

EVENT_CHOICES = [
    ('', 'Select event type'),
    ('wedding', 'Wedding'),
    ('birthday', 'Birthday Party'),
    ('corporate', 'Corporate Event'),
    ('engagement', 'Engagement/Introduction'),
    ('burial', 'Burial Ceremony'),
    ('other', 'Other'),
]

class BookingForm(forms.ModelForm):
    budget_range = forms.ChoiceField(
        choices=BUDGET_CHOICES,
        widget=forms.Select(attrs={'class': 'fi'})
    )
    event_type = forms.ChoiceField(
        choices=EVENT_CHOICES,
        widget=forms.Select(attrs={'class': 'fi'})
    )
    event_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'fi'})
    )

    class Meta:
        model = Booking
        fields = [
            'name', 'email', 'phone',
            'event_type', 'event_date',
            'budget_range', 'package', 'notes'
        ]