from django.contrib import admin
from .models import Table, Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'table', 'date', 'start_time', 'end_time', 'num_guests',
    ]
    search_fields = ['user__username', 'table__table_number', 'date']
    list_filter = ['date', 'num_guests']


admin.site.register(Table)
admin.site.register(Booking, BookingAdmin)
