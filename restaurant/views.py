from django.shortcuts import render
from django.http import HttpResponse

def my_restaurant(request):
    return HttpResponse("restaurant")

def home(request):
    return HttpResponse("Welcome to the Steakery!")

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def your_reservation_view(request):
    if request.method == 'POST':
        # Extract data from POST request
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        table_id = request.POST.get('table')

     

        # Respond with success
        return JsonResponse({'message': 'Booking successfully made!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

    from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

# Create a booking
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

# List all bookings
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)  # Filter bookings for logged-in user
    return render(request, 'booking_list.html', {'bookings': bookings})

# Update a booking
def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')  # Redirect to list of bookings
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_form.html', {'form': form})


# Delete a booking
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')  # Redirect to list of bookings
    return render(request, 'confirm_delete.html', {'booking': booking})