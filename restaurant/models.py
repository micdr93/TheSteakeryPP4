from django.db import models
from django.contrib.auth.models import User
from datetime import time, timedelta, datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

class SpecialRequest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    max_capacity = models.PositiveIntegerField(
        default=4, 
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    def __str__(self):
        return f"Table {self.table_number} - Max {self.max_capacity} guests"

class Booking(models.Model):
    WEEKDAY_OPENING_TIME = time(12, 0)
    WEEKDAY_CLOSING_TIME = time(22, 0)
    FRIDAY_SATURDAY_CLOSING_TIME = time(23, 0)
    SUNDAY_OPENING_TIME = time(11, 0)
    SUNDAY_CLOSING_TIME = time(21, 0)
    MAX_DINING_DURATION = timedelta(hours=2)
    MAX_ADVANCE_BOOKING_DAYS = 30

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(editable=False)
    num_guests = models.PositiveIntegerField(
        default=1, 
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    special_requests = models.ManyToManyField(SpecialRequest, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    additional_requests = models.TextField(blank=True, null=True, max_length=500)

    def clean(self):
        now = timezone.now().date()

        # Booking date validations
        if self.date < now:
            raise ValidationError("Reservation date must be in the future.")
        
        if (self.date - now).days > self.MAX_ADVANCE_BOOKING_DAYS:
            raise ValidationError(f"Bookings can only be made up to {self.MAX_ADVANCE_BOOKING_DAYS} days in advance.")

        # Time and operating hours validation
        day_of_week = self.date.weekday()
        if day_of_week < 4:  # Weekdays
            opening_time = self.WEEKDAY_OPENING_TIME
            closing_time = self.WEEKDAY_CLOSING_TIME
        elif day_of_week < 6:  # Friday and Saturday
            opening_time = self.WEEKDAY_OPENING_TIME
            closing_time = self.FRIDAY_SATURDAY_CLOSING_TIME
        else:  # Sunday
            opening_time = self.SUNDAY_OPENING_TIME
            closing_time = self.SUNDAY_CLOSING_TIME

        # Validate start time within operating hours
        if self.start_time < opening_time or self.start_time >= closing_time:
            raise ValidationError(f"Reservations must be between {opening_time.strftime('%I:%M %p')} and {closing_time.strftime('%I:%M %p')} on {self.date.strftime('%A')}.")

        # Calculate and validate end time
        self.end_time = (datetime.combine(self.date, self.start_time) + self.MAX_DINING_DURATION).time()
        if self.end_time > closing_time:
            raise ValidationError("The booking exceeds the restaurant's closing time.")

        # Table capacity validation
        if self.table and self.num_guests > self.table.max_capacity:
            raise ValidationError(f"Table {self.table.table_number} only accommodates {self.table.max_capacity} guests.")

        # Check for overlapping bookings
        overlapping_bookings = Booking.objects.filter(
            table=self.table,
            date=self.date,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(id=self.id)

        if overlapping_bookings.exists():
            raise ValidationError("This table is already booked for the selected time slot.")

    def save(self, *args, **kwargs):
        self.full_clean()
        self.end_time = (datetime.combine(self.date, self.start_time) + self.MAX_DINING_DURATION).time()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.id} - {self.user.username}, Table {self.table.table_number if self.table else 'Unassigned'}, {self.date} {self.start_time}"

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name