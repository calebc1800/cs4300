from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create router for API endpoints
router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'seats', views.SeatViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),
    
    # Template URLs
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/book/', views.seat_booking, name='book_seat'),
    path('history/', views.booking_history, name='booking_history'),
]
