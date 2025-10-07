from django.core.management.base import BaseCommand
from bookings.models import Movie, Seat
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Deletes all test movies, seats, and the test user."

    def handle(self, *args, **options):
        Movie.objects.all().delete()
        Seat.objects.all().delete()
        User = get_user_model()
        User.objects.filter(username="testuser01").delete()
        User.objects.filter(username="testuser02").delete()
        self.stdout.write(self.style.SUCCESS("Test data cleared."))
