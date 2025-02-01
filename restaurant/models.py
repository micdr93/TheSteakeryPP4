from django.db import models
from django.contrib.auth.models import User
from datetime import time, timedelta, datetime
from django.utils import timezone
from django.core.exceptions import ValidationError

class SpecialRequest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    max_capacity = models.PositiveIntegerField(default=4)

    def __str__(self):
        return f"Table {self.table_number} - Max Capacity: {self.max_capacity}"

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    WEEKDAY_OPENING_TIME = time(12, 0)  # 12:00 PM
    WEEKDAY_CLOSING_TIME = time(22, 0)  # 10:00 PM
    FRIDAY_SATURDAY_CLOSING_TIME = time(23, 0)  # 11:00 PM
    SUNDAY_OPENING_TIME = time(11, 0)  # 11:00 AM
    SUNDAY_CLOSING_TIME = time(21, 0)  # 9:00 PM
    MAX_DINING_DURATION = timedelta(hours=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
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

        day_of_week = self.date.weekday()
        if day_of_week < 4:  # Monday to Thursday
            opening_time = self.WEEKDAY_OPENING_TIME
            closing_time = self.WEEKDAY_CLOSING_TIME
        elif day_of_week < 6:  # Friday and Saturday
            opening_time = self.WEEKDAY_OPENING_TIME
            closing_time = self.FRIDAY_SATURDAY_CLOSING_TIME
        else:  # Sunday
            opening_time = self.SUNDAY_OPENING_TIME
            closing_time = self.SUNDAY_CLOSING_TIME

        if self.start_time < opening_time or self.start_time >= closing_time:
            raise ValidationError(f"Reservations must be between {opening_time.strftime('%I:%M %p')} and {closing_time.strftime('%I:%M %p')} on {self.date.strftime('%A')}.")

        self.end_time = (datetime.combine(self.date, self.start_time) + self.MAX_DINING_DURATION).time()

        if self.end_time > closing_time:
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