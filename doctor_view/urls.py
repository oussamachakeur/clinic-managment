from django.urls import path, include
from .views import DoctorDashboard ,DoctorUpdate



urlpatterns = [
    path('dashboard/' , DoctorDashboard.as_view() , name='reciptionDashboard'),
    path('dashboard/<int:pk>' , DoctorUpdate.as_view() ,name="doctorUpdate"),
]
