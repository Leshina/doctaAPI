from django.db import models
from django.contrib.auth import get_user_model
from Doctors.models import Doctor  

User = get_user_model()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  

    def __str__(self):
        return f'{self.user.username} - {self.doctor.name} - {self.date} - {self.time}'
