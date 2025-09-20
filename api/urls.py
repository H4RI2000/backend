from django.urls import path
from hosapp.views import AppointmentListCreateView, AppointmentListView
from hosapp.views import DoctorRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from hosapp.views import AppointmentDeleteView



urlpatterns = [
    path("appointments/", AppointmentListCreateView.as_view(), name="appointment-list-create"),  # GET + POST
    path("appointments/list/", AppointmentListView.as_view(), name="appointment-list"),          # GET only

    path("register-doctor/", DoctorRegisterView.as_view(), name="register-doctor"),
    path("login-doctor/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
    path("appointments/<int:pk>/", AppointmentDeleteView.as_view(), name="appointment-delete"),

    

]
