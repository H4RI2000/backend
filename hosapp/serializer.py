from rest_framework import serializers
from .models import Appointment
from django.contrib.auth.models import User
from .models import Doctor

class AppointmentSerializer(serializers.ModelSerializer):
    """
    A serializer to convert the Appointment model into a JSON representation.
    """
    class Meta:
        model = Appointment
        fields = '__all__'




class DoctorRegisterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=6)
    department = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["full_name", "email", "password", "department"]

    def create(self, validated_data):
        full_name = validated_data.pop("full_name")
        email = validated_data.pop("email")
        password = validated_data.pop("password")
        department = validated_data.pop("department")

        # Create user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=full_name
        )

        # Create doctor profile
        Doctor.objects.create(user=user, department=department)
        return user

