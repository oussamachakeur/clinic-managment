from django.urls import path , include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView 
from superuser_view import views
from users.views import DoctorProfileVS , ReceptionisProfile , PatientProfilesVS , DoctorsListVS , ReceptionistListVS , PatientListVS


urlpatterns = [
    path('dashboard/' , views.AdminStatsView.as_view() , name='dashboard'),
    path('dashboard/doctors' , DoctorsListVS.as_view() , name='doctors'),
    path('dashboard/receptionist' , ReceptionistListVS.as_view() , name='receptionist'),
    path('dashboard/patients' , PatientListVS.as_view() , name='patients'),
]