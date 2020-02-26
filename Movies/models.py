from django.db import models
from django.utils import timezone

class Movie_Info(models.Model):
    title = models.CharField(max_length=100)
    length = models.CharField(max_length=8)
    rating = models.CharField(max_length=3)
    date_released = models.DateTimeField()
    date_ending = models.DateTimeField()
    status = models.CharField(max_length=30)
    preview_photo = models.CharField(max_length=150)
    description = models.TextField(max_length=4000)
    link = models.TextField(max_length=300)

    def __str__(self):
        return self.title

class Session_Info(models.Model):
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    cinema = models.DecimalField(decimal_places=0, max_digits=3)
    price = models.CharField(max_length=8, default='$14.00')
    booking_link = models.TextField(default='/bookings/')
    title = models.ForeignKey(Movie_Info, on_delete=models.CASCADE)

    def __str__(self):
        id = str(self.title)

        return id
