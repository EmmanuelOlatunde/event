# bookings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('packages/', views.packages, name='packages'),
    path('book/', views.book, name='book'),
    path('book/<int:package_id>/', views.book, name='book_package'),
    path('booking/confirmed/<int:pk>/', views.booking_confirm, name='booking_confirm'),
]