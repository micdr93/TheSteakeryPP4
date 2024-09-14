from django.contrib import admin
from .models import Restaurant, Booking

# Register your models here.
class BookingAdmin (admin.ModelAdmin):

    list_display = [
    'id',
    'name',  # Name of the customer making the reservation
    'email',  # Email of the customer
    'phone',  # Phone number of the customer
    'date',  # Reservation date
    'time',  # Reservation time
    'guests',  # Number of guests
    'special_requests',  # Any special requests from the customer
    'created_at',  # When the reservation was created
]

search_fields = ['name', 'email', 'phone']  # Add search functionality
list_filter = ['date', 'guests']  # Add filters to make admin management easier

admin.site.register(Booking, BookingAdmin) 
admin.site.register(MenuItem) 