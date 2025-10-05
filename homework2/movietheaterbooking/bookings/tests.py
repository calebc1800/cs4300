from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date, timedelta
from .models import Movie, Seat, Booking

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie",
            release_date=date(2024, 1, 1),
            duration=timedelta(minutes=120)
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.duration, timedelta(minutes=120))
        self.assertEqual(str(self.movie), "Test Movie")

    def test_movie_ordering(self):
        movie2 = Movie.objects.create(
            title="Earlier Movie",
            description="An earlier movie",
            release_date=date(2023, 12, 1),
            duration=timedelta(minutes=90)
        )
        movies = Movie.objects.all()
        self.assertEqual(movies.first(), movie2)  # Should be ordered by release_date

class SeatModelTest(TestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="A01")

    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_number, "A01")
        self.assertEqual(self.seat.booking_status, False)
        self.assertEqual(str(self.seat), "Seat A01 - False")

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie",
            release_date=date(2024, 1, 1),
            duration=timedelta(minutes=120)
        )
        self.seat = Seat.objects.create(seat_number="A01")

    def test_booking_creation(self):
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )
        self.assertEqual(booking.movie, self.movie)
        self.assertEqual(booking.seat, self.seat)
        self.assertEqual(booking.user, self.user)
        self.assertTrue(booking.booking_date)

class MovieAPITest(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="API Test Movie",
            description="A test movie for API",
            release_date=date(2024, 1, 1),
            duration=timedelta(minutes=120)
        )

    def test_get_movies(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'API Test Movie')

    def test_create_movie(self):
        url = reverse('movie-list')
        data = {
            'title': 'New Movie',
            'description': 'A new movie',
            'release_date': '2024-02-01',
            'duration': timedelta(minutes=100)
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)

class SeatAPITest(APITestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="B01")

    def test_get_seats(self):
        url = reverse('seat-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_available_seats_endpoint(self):
        url = reverse('seat-available')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class TemplateViewTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Template Test Movie",
            description="A test movie for templates",
            release_date=date(2024, 1, 1),
            duration=timedelta(minutes=120)
        )

    def test_movie_list_view(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Template Test Movie")
        self.assertContains(response, "Available Movies")

    def test_seat_booking_view(self):
        response = self.client.get(reverse('book_seat', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.movie.title)
        self.assertContains(response, "Select Your Seat")
