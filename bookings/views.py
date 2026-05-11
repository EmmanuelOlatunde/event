# bookings/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Package, Booking
from .forms import BookingForm


# ── context shared across templates ─────────────────────────────────────────

STATS = [
    ("200+", "Events Planned"),
    ("98%",  "Client Satisfaction"),
    ("8+",   "Years Experience"),
]

SERVICES = [
    {"icon": "💍", "title": "Full Wedding Planning",   "description": "End-to-end coordination from engagement to your last dance. We handle everything so you simply enjoy the day."},
    {"icon": "🌸", "title": "Décor & Styling",         "description": "Transforming venues into breathtaking spaces that reflect your personality, taste, and love story."},
    {"icon": "📋", "title": "Day Coordination",        "description": "Our team ensures every moment runs on schedule, so you and your guests experience pure joy."},
    {"icon": "🤝", "title": "Vendor Management",       "description": "We source and manage trusted vendors — from caterers to photographers — and negotiate on your behalf."},
]

TESTIMONIALS = [
    {
        "quote":  "Elara Events made our wedding completely stress-free. Every detail we discussed was executed perfectly — from the florals to the timeline. Truly exceptional.",
        "author": "Adaeze & Emeka Okonkwo",
        "event":  "Traditional & White Wedding, April 2024",
    },
    {
        "quote":  "I was skeptical about using a planner, but working with Elara transformed our experience. They handled vendors we didn't even know we needed. Worth every kobo.",
        "author": "Bisi Adeleke",
        "event":  "Garden Wedding, February 2024",
    },
    {
        "quote":  "The booking system alone saved us so much time. No DMs, no confusion — just a clear process from day one. Our guests are still talking about the décor.",
        "author": "Ngozi & Tunde Bassey",
        "event":  "Lagos Wedding, December 2023",
    },
]

NEXT_STEPS = [
    "Our team reviews your request and checks availability",
    "We call or email you within 24 hours to confirm",
    "A consultation session is scheduled to plan your event",
]


# ── views ────────────────────────────────────────────────────────────────────

def home(request):
    packages = Package.objects.filter(is_active=True)[:3]
    return render(request, "bookings/home.html", {
        "packages":     packages,
        "stats":        STATS,
        "services":     SERVICES,
        "testimonials": TESTIMONIALS,
    })


def packages(request):
    all_packages = Package.objects.filter(is_active=True)
    return render(request, "bookings/packages.html", {
        "packages": all_packages,
    })


def book(request, package_id=None):
    selected_package = None
    if package_id:
        selected_package = get_object_or_404(Package, id=package_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect("booking_confirm", pk=booking.pk)
    else:
        initial = {}
        if selected_package:
            initial["package"] = selected_package
        form = BookingForm(initial=initial)

    return render(request, "bookings/book.html", {
        "form":             form,
        "selected_package": selected_package,
        "packages":         Package.objects.filter(is_active=True),
    })


def booking_confirm(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, "bookings/confirm.html", {
        "booking":    booking,
        "next_steps": NEXT_STEPS,
    })