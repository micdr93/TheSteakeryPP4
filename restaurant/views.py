from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required  # Import this decorator
from .models import Booking
from .forms import BookingForm

# Home view
def home(request):
    return render(request, 'home.html')

# About view
def about_view(request):
    return render(request, 'about.html')

# Contact view
def contact_view(request):
    return render(request, 'contact.html')

# Index view for the restaurant
def index(request):
    return render(request, 'index.html')

# Menu view
def menu_view(request):
    menu_items = "item"  
    return render(request, 'menu.html', {'menu_items': menu_items})

# Sign-up view for new users
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after sign-up
            return redirect('restaurant')  # Redirect to the index page after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Reservation view
@login_required
def your_reservation_view(request):
    if request.method == 'POST':
        # Extract data from POST request
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        table_id = request.POST.get('table')

        # Validate required fields
        if not all([date, time, guests, phone, email, table_id]):
            return JsonResponse({'error': 'Missing required fields.'}, status=400)

        return JsonResponse({'message': 'Booking successfully made!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

# Bookings view
@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)  
    return render(request, 'bookings.html', {'bookings': bookings})

# CRUD Views for Booking
@login_required
def create_booking(request):
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

@login_required
def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')  # Redirect to the list of bookings
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_form.html', {'form': form})

@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')  # Redirect to the list of bookings
    return render(request, 'confirm_delete.html', {'booking': booking})
