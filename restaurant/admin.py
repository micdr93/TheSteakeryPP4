from django.contrib import admin
from .models import Table, Booking

# Register your models here.
class BookingAdmin (admin.ModelAdmin):

    list_display = [
    'id',
    'user_name',  # Name of the customer making the reservation
    'user_email',  # Email of the customer
    'user_phone',  # Phone number of the customer
    'date',  # Reservation date
    'time',  # Reservation time
    'num_guests',  # Number of guests
    'get_special_requests',  # Any special requests from the customer
    'created_at',  # When the reservation was created
]

    search_fields = ['user__name', 'user__email', 'user__phone']  # Add search functionality    
    list_filter = ['date', 'num_guests']  # Add filters to make admin management easier

    def user_name (self, obj) :
        return obj.user.username

    def user_email (self, obj) :
        return obj.user.email

    def user_phone (self, obj) :
        return obj.user.phone

    def user_email (self, obj) :
        return obj.user.email

    def get_special_requests(self, obj):
        return ", ".join([request.name for request in obj.special_requests.all()])

    user_name.short_description = "Name"
    user_email.short_description = "Email"
    user_phone.short_description = "Phone"
    get_special_requests.short_description = "Special Requests"
  

admin.site.register(Table)

admin.site.register(Booking, BookingAdmin) 
 