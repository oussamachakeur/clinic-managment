from rest_framework import serializers
from core.models import CustomUser , Patient , Doctor , Receptionist ,Booking



class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = ['doctor','reason']
        
    def create(self, validated_data):
        request = self.context['request']
        user = request.user

        # Get the Patient object for the current user
        try:
            patient = Patient.objects.get(user=user)
        except Patient.DoesNotExist:
            raise serializers.ValidationError("Logged in user is not a patient.")

        # Create booking with patient auto-filled
        booking = Booking.objects.create(
            patient=patient,
            **validated_data
        )
        return booking
            