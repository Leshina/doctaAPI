# models.py
import uuid
from django.db import models

class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    is_available = models.BooleanField(default=False)

class DoctorAvailability(models.Model):
    doctor = models.ForeignKey('Doctor', related_name='availabilities', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.doctor.name} - {self.date} {self.start_time}-{self.end_time}'
