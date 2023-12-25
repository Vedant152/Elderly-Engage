from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], null=True)
    area = models.CharField(max_length=50, blank=False, null=False)
    city = models.CharField(max_length=30, blank=False, null=False)
    pincode = models.IntegerField(validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    email = models.EmailField(blank=False, null=False, unique=True)
    phone = models.CharField(max_length=13, blank=True, null=True, default="")
    about = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('health', 'Health'),
        ('social', 'Social'),
    ]
    event_name = models.CharField(max_length=60, blank=False, null=False)
    event_description = models.CharField(max_length=1000, null=True)
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES, null=True)
    event_date = models.DateField(null=False)
    event_starttime = models.TimeField(null=False)
    event_endtime = models.TimeField(null=False)
    event_venue = models.CharField(max_length=30, blank=False, null=False)
    event_area = models.CharField(max_length=50, blank=False, null=False)
    event_city = models.CharField(max_length=30, blank=False, null=False)
    event_pincode = models.IntegerField(validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    approved = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)
    user_recommended = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.event_name + " [ " + self.event_area + ", " + self.event_city + " ]"
    

class Registration(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=None)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.person.name} - {self.event.event_name}"