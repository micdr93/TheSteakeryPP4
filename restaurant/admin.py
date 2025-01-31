from django.contrib import admin
from django.contrib.auth.models import User
from .models import Table, Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'table', 'date', 'start_time', 'end_time', 'num_guests', 'created_at']


    search_fields = ['user__username', 'user__email', 'user__profile__phone']  # Add search functionality to search by profile phone    
    list_filter = ['date', 'num_guests']  # Add filters to make admin management easier

    def user_name(self, obj):
        return obj.user.username

    def user_email(self, obj):
        return obj.user.email

    def user_phone(self, obj):
        return obj.user.profile.phone if hasattr(obj.user, 'profile') else 'N/A'

    def get_special_requests(self, obj):
        return ", ".join([request.name for request in obj.special_requests.all()])

    user_name.short_description = "Name"
    user_email.short_description = "Email"
    user_phone.short_description = "Phone"
    get_special_requests.short_description = "Special Requests"


admin.site.register(Table)
admin.site.register(Booking, BookingAdmin)
