from django.shortcuts import render
from rest_framework import viewsets , status
from .serializers import CustomUserSerializer , DoctorSerializer , PatientSerializer  ,ReceptionistSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import generics
from core.models import Doctor , Receptionist,Patient
from rest_framework.exceptions import PermissionDenied


class UserRegistrationVS(viewsets.ModelViewSet):
    queryset= get_user_model().objects.all()
    serializer_class= CustomUserSerializer
    
    def create(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data= request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        
        return Response(self.get_serializer(user).data, status=status.HTTP_201_CREATED)

class DoctorsListVS(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    def get_queryset(self):
        user= self.request.user
        if user.is_staff or user.is_superuser :
            return Doctor.objects.all()
        elif hasattr(user, "Doctor_profile"):
            return Doctor.objects.filter(user=user)
        elif hasattr(user ,"Receptionist_name"):
            return Doctor.objects.all()
    
        
class DoctorProfileVS(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    def get_object(self):
        doctor = super().get_object()  
        user = self.request.user
        if user.is_staff or user.is_superuser or hasattr(user ,"Receptionist_name"):
            return doctor  
        elif hasattr(user, 'Doctor_profile') and user.Doctor_profile == doctor:
            return doctor  
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


class ReceptionistListVS(generics.ListAPIView):
    queryset = Receptionist.objects.all()
    serializer_class = ReceptionistSerializer
    
    def get_queryset(self):
        user= self.request.user
        if user.is_staff or user.is_superuser :
            return Receptionist.objects.all()
        elif hasattr(user, "Receptionist_name"):
            return Receptionist.objects.filter(user=user)
       

class ReceptionisProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset= Receptionist.objects.all()
    serializer_class = ReceptionistSerializer
    
    def get_object(self):
        receptionist= super().get_object()
        user  =self.request.user
        if user.is_staff or user.is_superuser:
            return receptionist
        elif hasattr(user , 'Receptionist_name') and user.Receptionist_name == receptionist :
            return receptionist
        else:
            raise PermissionDenied("You don't have permission to access this profile.")  
        
    def update(self, request, *args, **kwargs):
        user = self.request.user
        if not (user.is_superuser or user.is_staff):
            raise PermissionDenied("Only superuser  can update this profile.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        if not (user.is_superuser or user.is_staff ):
            raise PermissionDenied("Only superuser can delete this profile.")
        return super().destroy(request, *args, **kwargs)


class PatientListVS(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user ,'Patient_name'):
            return Patient.objects.filter(user=user)
        else:
            return Patient.objects.all()

class PatientProfilesVS(generics.RetrieveUpdateDestroyAPIView):
    queryset= Patient.objects.all()
    serializer_class= PatientSerializer
    
    def get_object(self):
        patient = super().get_object()  
        user = self.request.user
        if user.is_staff or user.is_superuser or hasattr(user ,"Receptionist_name") or hasattr(user ,"Doctor_profile"):
            return patient  
        elif hasattr(user, 'Patient_name') and user.Patient_name == patient:
            return patient  
        else:
            raise PermissionDenied("You don't have permission to access this profile.")
        
        
    def update(self, request, *args, **kwargs):
        user = self.request.user 
        if not (hasattr(user , 'Patient_name')):
            raise PermissionDenied('only user can edit his/her profile')
        return super().update(request, *args, **kwargs)
    
    
    def delete(self, request, *args, **kwargs):
        user = self.request.user 
        if not (hasattr(user , 'Patient_name')):
            raise PermissionDenied('only user can delete his/her profile')
        return super().delete(request, *args, **kwargs)
        