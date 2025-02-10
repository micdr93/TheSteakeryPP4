from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from restaurant import views as restaurant_views

urlpatterns = [
    # Home page
    path('', restaurant_views.home, name='home'),

    # Restaurant index page
    path('restaurant/', restaurant_views.index, name='restaurant'),

    # Contact page
    path('contact/', restaurant_views.contact_view, name='contact'), 
    # About page
    path('about/', restaurant_views.about_view, name='about'),

    # Menu page
    path('menu/', restaurant_views.menu_view, name='menu'),

    # Bookings: CRUD operations
    path('bookings/', restaurant_views.booking_list, name='booking_list'),
    path('bookings/create/', restaurant_views.create_booking, 
         name='create_booking'),
    path('bookings/update/<int:pk>/', restaurant_views.update_booking, 
         name='update_booking'),
    path('bookings/delete/<int:pk>/', restaurant_views.delete_booking, 
         name='delete_booking'),
    # Authentication views using Django's built-in views for login/logout
    # Log-in page with custom template
    # Log-out functionality with redirect to home
    path(
        'logout/', 
        auth_views.LogoutView.as_view(next_page='home'),
        name='logout'
    ),
    path(
        'login/', 
        auth_views.LoginView.as_view(template_name='registration/login.html'), 
        name='login'
    ),
    path('signup/', restaurant_views.signup, name='signup'),

    # Admin site
    path('admin/', admin.site.urls),

    # Admin bookings
    path(
        'admin_bookings/',
        restaurant_views.admin_booking_list,
        name='admin_booking_list'
    ),
    path(
        'admin_bookings/<int:pk>/edit/',
        restaurant_views.admin_update_booking,
        name='admin_update_booking'
    ),
    path(
        'admin_bookings/<int:pk>/delete/',
        restaurant_views.admin_delete_booking,
        name='admin_delete_booking'
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
