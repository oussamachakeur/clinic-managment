from django.shortcuts import render
from .serializers import DoctorDasboardSerializer
from rest_framework import  generics
from core.models import Booking
from rest_framework.exceptions import PermissionDenied


class DoctorDashboard(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = DoctorDasboardSerializer
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'Doctor_profile') or user.is_superuser:
            return Booking.objects.filter(doctor= user.Doctor_profile, status='accepted')
        
        raise PermissionDenied("Only doctors can access this view.")


class DoctorUpdate(generics.RetrieveUpdateAPIView):
    queryset= Booking.objects.all()
    serializer_class= DoctorDasboardSerializer
    
    def get_object(self):
        booking=super().get_object()
        user = self.request.user
        if hasattr(user, 'Doctor_profile') :
            return booking
        raise PermissionDenied("You don't have permission to access this profile.") 
    
    def update(self, request, *args, **kwargs):
        user = self.request.user
        if not (user.is_superuser or user.is_staff or hasattr(user ,"Doctor_profile")):
            raise PermissionDenied("Only doctor can update this.")
        return super().update(request, *args, **kwargs)