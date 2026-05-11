# bookings/models.py

from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    features = models.TextField(help_text="One feature per line")
    starting_price = models.CharField(max_length=50)  # e.g. "₦150,000"
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_features_list(self):
        return [f.strip() for f in self.features.splitlines() if f.strip()]


class Booking(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('confirmed', 'Confirmed'),
        ('declined', 'Declined'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    event_type = models.CharField(max_length=100)
    event_date = models.DateField()
    budget_range = models.CharField(max_length=50)
    package = models.ForeignKey(
        Package, on_delete=models.SET_NULL, null=True, blank=True
    )
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.event_date} ({self.status})"