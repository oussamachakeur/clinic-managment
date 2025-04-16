from rest_framework import serializers
from core.models import CustomUser , Patient , Doctor , Receptionist ,Booking



class DoctorDasboardSerializer(serializers.ModelSerializer):
    patient = serializers.CharField(source='patient.user.username', read_only=True)
    doctor = serializers.CharField(source='doctor.user.username' ,read_only=True)
    appointment_details = serializers.CharField(read_only=False)
    class Meta:
        model = Booking 
        fields = ['id','doctor','patient','reason','appointment_date','appointment_time','created_at','receptionist','status','appointment_details']