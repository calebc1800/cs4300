from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import timedelta

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'duration']
        
    def validate_duration(self, value):
        if value <= timedelta(0):
            raise serializers.ValidationError("Duration must be positive")
        return value

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'booking_status']
        
    def validate_seat_number(self, value):
        if not value.strip():
            raise serializers.ValidationError("Seat number cannot be empty")
        return value

class BookingSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    seat_number = serializers.CharField(source='seat.seat_number', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'movie', 'seat', 'user', 'booking_date', 'movie_title', 'seat_number', 'user_username']
        read_only_fields = ['booking_date']
        
    def validate(self, data):
        # Check if seat is available
        seat = data.get('seat')
        if seat and seat.booking_status:
            raise serializers.ValidationError("This seat is already booked")
        return data

    def create(self, validated_data):
        # Mark seat as booked when creating booking
        booking = super().create(validated_data)
        booking.seat.booking_status = True
        booking.seat.save()
        return booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
