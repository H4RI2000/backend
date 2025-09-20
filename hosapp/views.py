from rest_framework import generics,status
from rest_framework.response import Response
from hosapp.serializer import DoctorRegisterSerializer
from django.contrib.auth.models import User
from .models import Appointment
from hosapp.serializer import AppointmentSerializer
from rest_framework.permissions import AllowAny

from rest_framework.permissions import IsAuthenticated, AllowAny
from hosapp.serializer import AppointmentSerializer


class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all().order_by("-preferred_date", "-preferred_time")
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny] 


# Get all appointments (GET)
class AppointmentListView(generics.ListAPIView):
    queryset = Appointment.objects.all().order_by("-preferred_date", "-preferred_time")

    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated] 





class DoctorRegisterView(generics.CreateAPIView):
    serializer_class = DoctorRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "Doctor registered successfully"}, status=status.HTTP_201_CREATED)
    





class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all().order_by("-preferred_date", "-preferred_time")
    serializer_class = AppointmentSerializer
   

class AppointmentDeleteView(generics.DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
 



