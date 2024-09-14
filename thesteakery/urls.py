"""
URL configuration for thesteakery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from restaurant import views as restaurant_views  # Import views from the restaurant app

urlpatterns = [
    path('', restaurant_views.home, name='home'),  # Home page
    path('restaurant/', restaurant_views.my_restaurant, name='restaurant'),  # Restaurant simple view
    path('menu/', restaurant_views.menu_view, name='menu'),  # Menu view to display menu items

    # Bookings: CRUD operations
    path('bookings/', restaurant_views.booking_list, name='booking_list'),  # Read (list bookings)
    path('bookings/create/', restaurant_views.create_booking, name='create_booking'),  # Create booking
    path('bookings/update/<int:pk>/', restaurant_views.update_booking, name='update_booking'),  # Update booking
    path('bookings/delete/<int:pk>/', restaurant_views.delete_booking, name='delete_booking'),  # Delete booking

    path('admin/', admin.site.urls),  # Admin site
]