from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    realse_date = models.DateField()
    duration = models.DurationField()

class Seat(models.Model):
    seat_number = models.IntegerField()
    booking_status = models.BooleanField(default=False)

class Booking(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = "test user"
    booking_date = models.DateField()
