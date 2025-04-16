from django.shortcuts import render
from .serializers import DashboardBooking
from rest_framework import viewsets , status , generics
from core.models import Booking
from rest_framework.exceptions import PermissionDenied



class BookingList(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = DashboardBooking
    def get_queryset(self):
        user= self.request.user
        if user.is_staff or user.is_superuser:
            return Booking.objects.all()
        elif hasattr(user ,"Receptionist_name"):
            return Booking.objects.all()
    
    
    
    
class BookingManageVS(generics.RetrieveUpdateDestroyAPIView):
    queryset= Booking.objects.all()
    serializer_class= DashboardBooking
    def get_object(self):
        booking = super().get_object()  
        user = self.request.user
        if user.is_staff or user.is_superuser or hasattr(user ,"Receptionist_name"):
            return booking  
        else:
            raise PermissionDenied("You don't have permission to access this profile.")

    def update(self, request, *args, **kwargs):
        user = self.request.user
        if not (user.is_superuser or user.is_staff or hasattr(user ,"Receptionist_name")):
            raise PermissionDenied("Only superuser or receptionist can update doctor profiles.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        if not (user.is_superuser or user.is_staff or hasattr(user ,"Receptionist_name")):
            raise PermissionDenied("Only superuser or receptionist can delete doctor profiles.")
        return super().destroy(request, *args, **kwargs)