# bookings/management/commands/create_test_data.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from datetime import date, timedelta

from bookings.models import Movie, Seat

class Command(BaseCommand):
    help = "Create the database with test movies, seats, and a test user."

    def handle(self, *args, **options):
        # Create movies
        movie1, created = Movie.objects.get_or_create(
            title="The Amazing Spider-Man",
            defaults={
                "description": "A young Peter Parker discovers his powers and becomes Spider-Man.",
                "release_date": date(2024, 1, 15),
                "duration": timedelta(minutes=142),
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Created movie: {movie1.title}"))
        else:
            self.stdout.write(self.style.WARNING(f"Movie already exists: {movie1.title}"))

        movie2, created = Movie.objects.get_or_create(
            title="Inception",
            defaults={
                "description": "A thief who steals corporate secrets through dream-sharing technology.",
                "release_date": date(2024, 2, 1),
                "duration": timedelta(minutes=148),
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Created movie: {movie2.title}"))
        else:
            self.stdout.write(self.style.WARNING(f"Movie already exists: {movie2.title}"))

        # Create seats
        seat_count = 0
        for row in ("A", "B"):
            for i in range(1, 21):
                seat_number = f"{row}{i:02d}"
                seat, created = Seat.objects.get_or_create(seat_number=seat_number)
                if created:
                    seat_count += 1

        self.stdout.write(self.style.SUCCESS(f"Created {seat_count} new seats."))

        # Create test user
        User = get_user_model()
        username = "testuser"
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(
                username=username,
                email="testuser@example.com",
                password="password123"
            )
            self.stdout.write(self.style.SUCCESS(f"Created test user: {username}"))
        else:
            self.stdout.write(self.style.WARNING(f"Test user already exists: {username}"))

        self.stdout.write(self.style.SUCCESS("Test data and test user created successfully!"))
