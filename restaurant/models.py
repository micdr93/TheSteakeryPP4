from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta, time, datetime

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
    OPENING_TIME = time(12, 0)  # 12:00 PM
    CLOSING_TIME = time(23, 0)  # 11:00 PM
    MAX_DINING_DURATION = timedelta(hours=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=False)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(editable=False)
    num_guests = models.PositiveIntegerField(default=1)
    special_requests = models.ManyToManyField(SpecialRequest, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        now = timezone.now()
        if self.date < now.date() or (self.date == now.date() and self.start_time < now.time()):
            raise ValidationError("Reservation date and time must be in the future.")

        if self.table and self.num_guests > self.table.max_capacity:
            raise ValidationError(f"The table only accommodates {self.table.max_capacity} guests.")

        if self.start_time < self.OPENING_TIME or self.start_time >= self.CLOSING_TIME:
            raise ValidationError(f"Reservations must be between {self.OPENING_TIME.strftime('%I:%M %p')} and {self.CLOSING_TIME.strftime('%I:%M %p')}.")

        self.end_time = (datetime.combine(self.date, self.start_time) + self.MAX_DINING_DURATION).time()

        if self.end_time > self.CLOSING_TIME:
            raise ValidationError("The booking exceeds the restaurant's closing time.")

        overlapping_bookings = Booking.objects.filter(
            table=self.table,
            date=self.date,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(id=self.id)

        if overlapping_bookings.exists():
            raise ValidationError("This table is already booked for the selected time slot.")

    def save(self, *args, **kwargs):
        self.end_time = (datetime.combine(self.date, self.start_time) + self.MAX_DINING_DURATION).time()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.id} - User: {self.user.username}, Table {self.table.table_number}, Date: {self.date}, Time: {self.start_time}-{self.end_time}"