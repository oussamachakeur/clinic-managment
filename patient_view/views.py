from django.shortcuts import render
from .serializers import BookingSerializer
from rest_framework import viewsets , status , generics
from core.models import Booking




class BookingVS(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


