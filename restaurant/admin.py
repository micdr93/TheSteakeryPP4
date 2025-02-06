from django.contrib import admin
from .models import Table, Booking, SpecialRequest

class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'table', 'date', 'start_time', 'end_time', 'num_guests', 'get_special_requests']
    search_fields = ['user__username', 'table__table_number', 'date']
    list_filter = ['date', 'num_guests']

    def get_special_requests(self, obj):
        return ", ".join([request.name for request in obj.special_requests.all()])
    get_special_requests.short_description = "Special Requests"

admin.site.register(Table)
admin.site.register(Booking, BookingAdmin)
admin.site.register(SpecialRequest)