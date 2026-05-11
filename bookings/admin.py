# bookings/admin.py

from django.contrib import admin
from .models import Package, Booking

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'starting_price', 'is_active']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'event_type', 'event_date', 'package', 'status', 'created_at']
    list_filter = ['status', 'event_type']
    list_editable = ['status']  # change status inline in the list
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['created_at']