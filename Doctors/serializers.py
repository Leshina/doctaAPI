# serializers.py
from rest_framework import serializers
from .models import Doctor, DoctorAvailability

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = ['date', 'start_time', 'end_time']

class DoctorSerializer(serializers.ModelSerializer):
    availabilities = DoctorAvailabilitySerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'organization', 'email', 'phone', 'image', 'is_available', 'availabilities']
