from rest_framework import serializers
from core.models import CustomUser , Doctor , Receptionist , Patient
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _





class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'role']
    
    def create(self, validated_data):
        role = validated_data.get('role')
        
        status = 'accepted' if role == 'patient' else 'pending'
        
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=role,
            status=status
        )

        return user
    
class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    
    
class DoctorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Doctor
        fields = ['id', 'username','email','speciality','license_number','room_number','qualifications','address','languages_spoken' ,'phone','emergency_contact','is_available','image']


class ReceptionistSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Receptionist
        fields = ['id', 'username','email','department','shift','address','date_of_birth','languages_spoken','start_date','phone','emergency_contact','is_available']
        
class PatientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Patient
        fields = ['id', 'username','email','date_of_birth','address','start_date','phone','emergency_contact']