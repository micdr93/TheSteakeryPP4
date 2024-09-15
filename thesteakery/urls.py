from django.contrib import admin
from django.urls import path
from restaurant import views as restaurant_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home page
    path('', restaurant_views.home, name='home'),

    # Restaurant index page
    path('restaurant/', restaurant_views.index, name='restaurant'),

    # Contact page
    path('contact/', restaurant_views.contact_view, name='contact'), 

    # Menu page
    path('menu/', restaurant_views.menu_view, name='menu'),

    # Bookings: CRUD operations
    path('bookings/', restaurant_views.booking_list, name='booking_list'),  # List all bookings (Read)
    path('bookings/create/', restaurant_views.create_booking, name='create_booking'),  # Create a booking
    path('bookings/update/<int:pk>/', restaurant_views.update_booking, name='update_booking'),  # Update a booking
    path('bookings/delete/<int:pk>/', restaurant_views.delete_booking, name='delete_booking'),  # Delete a booking

    # Authentication views using Django's built-in views for login/logout
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Log-in page
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Log-out functionality with redirect to home
    path('signup/', restaurant_views.signup, name='signup'),  # Custom sign-up view

    # Admin site
    path('admin/', admin.site.urls),
]
