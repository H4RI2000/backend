from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Appointment(models.Model):
    """
    A Django model to store appointment booking details.
    """
    DEPARTMENT_CHOICES = [
        ('General Medicine', 'General Medicine'),
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
    ]

    TIME_CHOICES = [
        ('9:00 am to 10:30 am', '9:00 am to 10:30 am'),
        ('11:00 am to 1:00 pm', '11:00 am to 1:00 pm'),
        ('2:30 pm to 3:30 pm', '2:30 pm to 3:30 pm'),
        ('4:00 pm to 5:00 pm', '4:00 pm to 5:00 pm'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    preferred_date = models.DateField()
    preferred_time = models.CharField(max_length=50, choices=TIME_CHOICES)
    additional_requirements = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment for {self.full_name} on {self.preferred_date}"

    class Meta:
        verbose_name_plural = "Appointments"
        ordering = ['-preferred_date', 'full_name']

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor_profile")
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

