from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer, UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    @action(detail=True, methods=['get'])
    def available_seats(self, request, pk=None):
        """
        Get available seats for a specific movie
        """
        movie = self.get_object()
        available_seats = Seat.objects.filter(booking_status=False)
        serializer = SeatSerializer(available_seats, many=True)
        return Response({
            'movie': movie.title,
            'available_seats': serializer.data
        })
        
    @action(detail=True, methods=['get'])
    def unavailable_seats(self, request, pk=None):
        """
        Get unavailable (booked) seats for a specific movie
        """
        movie = self.get_object()
        unavailable_seats = Seat.objects.filter(movie=movie, booking_status=True)
        serializer = SeatSerializer(unavailable_seats, many=True)
        return Response({
            'movie': movie.title,
            'unavailable_seats': serializer.data
        })

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    
    @action(detail=False, methods=['get'])
    def available(self, request):
        """
        Get all available seats
        """
        available_seats = Seat.objects.filter(booking_status=False)
        serializer = self.get_serializer(available_seats, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def unavailable(self, request):
        """
        Get all unavailable seats
        """
        available_seats = Seat.objects.filter(booking_status=True)
        serializer = self.get_serializer(available_seats, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def book(self, request, pk=None):
        """
        Book a specific seat
        """
        seat = self.get_object()
        if seat.booking_status:
            return Response(
                {'error': 'Seat is already booked'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # This would typically create a booking, but will handle that in BookingViewSet
        return Response({'message': 'Use booking endpoint to complete booking'})

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        """
        Filter bookings by user if specified
        """
        queryset = Booking.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset
    
    @action(detail=False, methods=['get'])
    def my_bookings(self, request):
        """
        Get current user's bookings
        """
        if not request.user.is_authenticated:
            return Response(
                {'error': 'Authentication required'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        bookings = Booking.objects.filter(user=request.user)
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)

# Template Views for Web Interface
def movie_list(request):
    """
    Display list of movies
    """
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def seat_booking(request, movie_id):
    """
    Display seat booking page for a specific movie
    """
    movie = get_object_or_404(Movie, id=movie_id)
    # available_seats = Seat.objects.filter(booking_status=False)
    # unavailable_seats = Seat.objects.filter(booking_status=True)
    all_seats = Seat.objects.all()
    all_users = User.objects.filter(is_active=True)
    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        # 'available_seats': available_seats,
        # 'unavailable_seats': unavailable_seats,
        'all_seats': all_seats,
        'all_users': all_users
    })

def booking_history(request):
    """
    Display individual user's booking history - NO authentication required
    Simplified version without stats or "all users" view
    """
    # Get selected user from query parameters
    selected_user_id = request.GET.get('user_id')

    # Get ALL users for the dropdown
    all_users = User.objects.filter(is_active=True)

    # Get bookings only for selected user (no default "all bookings" view)
    if selected_user_id:
        try:
            selected_user = User.objects.get(id=selected_user_id, is_active=True)
            bookings = Booking.objects.filter(user=selected_user).order_by('-booking_date')
        except (User.DoesNotExist, ValueError):
            bookings = Booking.objects.none()
    else:
        # No user selected - show empty bookings
        bookings = Booking.objects.none()

    # Optimize database queries
    bookings = bookings.select_related('movie', 'seat', 'user')

    # Simple context data
    context = {
        'bookings': bookings,
        'all_users': all_users,
        'selected_user_id': int(selected_user_id) if selected_user_id else None,
    }

    return render(request, 'bookings/booking_history.html', context)

from django.views.decorators.http import require_http_methods

# Simple API endpoint
@require_http_methods(["GET"])
def get_user_bookings_api(request, user_id):
    """
    API endpoint to get bookings for a specific user - NO authentication required
    Simplified version without stats calculation
    """
    try:
        user = User.objects.get(id=user_id, is_active=True)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    # Get bookings for this user
    bookings = Booking.objects.filter(user=user).select_related(
        'movie', 'seat', 'user'
    )

    # Serialize bookings data
    bookings_data = []
    for booking in bookings:
        bookings_data.append({
            'id': booking.id,
            'movie_id': booking.movie.id,
            'movie_title': booking.movie.title,
            'movie_description': booking.movie.description,
            'movie_duration': booking.movie.duration,
            'movie_release_date': booking.movie.release_date.isoformat() if booking.movie.release_date else None,
            'seat_number': booking.seat.seat_number,
            'booking_date': booking.booking_date.isoformat(),
            'user_id': booking.user.id,
            'username': booking.user.username,
        })

    # Simple response
    return JsonResponse({
        'bookings': bookings_data,
        'user': {
            'id': user.id,
            'username': user.username,
        }
    })
