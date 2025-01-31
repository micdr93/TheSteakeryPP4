from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta, time

class SpecialRequest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    max_capacity = models.PositiveIntegerField(default=4)

    def __str__(self):
        return f"Table {self.table_number} - Max Capacity: {self.max_capacity}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=False)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    num_guests = models.PositiveIntegerField(default=1)
    special_requests = models.ManyToManyField(SpecialRequest, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    OPENING_TIME = time(12, 0)
    CLOSING_TIME = time(23, 0)
    MAX_DURATION = timedelta(hours=2)
    
    def clean(self):
        now = timezone.now()
        booking_datetime = timezone.datetime.combine(self.date, self.start_time)
        
        if booking_datetime < now:
            raise ValidationError("Reservation must be in the future.")
        
        if self.start_time < self.OPENING_TIME or self.end_time > self.CLOSING_TIME:
            raise ValidationError("Booking must be within restaurant hours (12 PM - 11 PM).")
        
        if (timezone.datetime.combine(self.date, self.end_time) - 
            timezone.datetime.combine(self.date, self.start_time)) > self.MAX_DURATION:
            raise ValidationError("Maximum dining duration is 2 hours.")
        
        if self.table and self.num_guests > self.table.max_capacity:
            raise ValidationError(f"The table only accommodates {self.table.max_capacity} guests.")
        
        overlapping_bookings = Booking.objects.filter(
            table=self.table, 
            date=self.date,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(id=self.id)
        
        if overlapping_bookings.exists():
            raise ValidationError("This table is already booked during the selected time.")
    
    def save(self, *args, **kwargs):
        if not self.end_time:
            self.end_time = (timezone.datetime.combine(self.date, self.start_time) + self.MAX_DURATION).time()
        super().save(*args, **kwargs)

    def __str__(self):
        return (f"Booking {self.id} - User: {self.user.username}, Table: {self.table.table_number}, "
                f"Date: {self.date}, Time: {self.start_time} - {self.end_time}")
