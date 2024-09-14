from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import MenuItem, Booking
from .forms import BookingForm
def my_restaurant(request):
    return HttpResponse("restaurant")
# General Restaurant Views

def home(request):
    """Home page view"""
    return HttpResponse("Welcome to the Steakery!")

def my_restaurant(request):
    """Simple Restaurant page view"""
    return HttpResponse("restaurant")

def menu_view(request):
    """Displays all menu items"""
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

# Authentication Views

def signup(request):
    """Sign-up view for new users"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after sign-up
            return redirect('home')  # Redirect to the home page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Reservation Views

@csrf_exempt
def your_reservation_view(request):
    """Handles a reservation through a POST request"""
    if request.method == 'POST':
        # Extract data from POST request
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        table_id = request.POST.get('table')

        # Additional logic to save the reservation could go here

        # Respond with success
        return JsonResponse({'message': 'Booking successfully made!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

    # Booking CRUD Operations
def create_booking(request):
    """Create a new booking"""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assuming the user is logged in
            booking.save()
            return redirect('booking_list')  # Redirect to list of bookings
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})


def booking_list(request):
    """List all bookings for the logged-in user"""
    bookings = Booking.objects.filter(user=request.user)  # Filter bookings for the logged-in user
    return render(request, 'booking_list.html', {'bookings': bookings})


def update_booking(request, pk):
    """Update an existing booking"""
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')  # Redirect to the list of bookings
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_form.html', {'form': form})



def delete_booking(request, pk):
    """Delete an existing booking"""
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')  # Redirect to the list of bookings
    return render(request, 'confirm_delete.html', {'booking': booking})