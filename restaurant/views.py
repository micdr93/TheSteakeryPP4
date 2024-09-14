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