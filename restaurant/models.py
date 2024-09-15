from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class SpecialRequest(models.Model):
    """
    Add a special request (e.g., vegetarian, wheelchair access) for reservations.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Table(models.Model):
    """
    A Table in the restaurant that can be reserved by guests.
    """
    table_number = models.PositiveIntegerField(unique=True)
    max_capacity = models.PositiveIntegerField(default=4)

    def __str__(self):
        return f"Table {self.table_number} - Max Capacity: {self.max_capacity}"


class Booking(models.Model):
    """
    Restaurant Booking
    This class handles the information related to a booking made by a user
    for a table reservation at The Steakery. It stores details such as the user
    who made the booking, reservation date and time, the number of guests,
    and any special requests.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=False)  # Reference to Table
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField(default=1)
    special_requests = models.ManyToManyField(SpecialRequest, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """
        Ensure the reservation date and time are in the future and guests
        do not exceed table capacity.
        """
        if self.date < timezone.now().date() or (self.date == timezone.now().date() and self.time < timezone.now().time()):
            raise ValidationError("Reservation date and time must be in the future.")

        # Ensure the number of guests doesn't exceed the table's capacity
        if self.table and self.num_guests > self.table.max_capacity:
            raise ValidationError(f"The table only accommodates {self.table.max_capacity} guests.")

    def __str__(self):
        return f"Booking {self.id} - User: {self.user.username}, Date: {self.date}, Time: {self.time}"
