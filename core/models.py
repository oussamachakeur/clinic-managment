from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os


def Doctor_image_file_path(instance, filename):
    
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'recipe', filename)



class CustomUser(AbstractUser):
    
    USER_TYPES = (
        ('doctor','Doctor'),
        ('patient','Patient'),
        ('receptionist','Receptionist'),
    )
    
    STATUS=(
        ('pending' , 'Pending'),
        ('accepted','Accepted'),
        ('rejected','Rejected'),
    )
    
    role = models.CharField(max_length=20 , choices=USER_TYPES , default='patient')
    status = models.CharField(max_length=20 , choices=STATUS , default='pending')
    
    
class Doctor(models.Model):
    SPECIALITIES = [
        ('GP', 'General Practitioner'),
        ('PED', 'Pediatrician'),
        ('GYNE', 'Gynecologist'),
        ('DERM', 'Dermatologist'),
        ('CARD', 'Cardiologist'),
        ('ORTHO', 'Orthopedic Surgeon'),
        ('NEURO', 'Neurologist'),
        ('PSY', 'Psychiatrist'),
        ('DENT', 'Dentist'),
        ('OPHTH', 'Ophthalmologist'),
        ('ENT', 'ENT Specialist'),
        ('ENDO', 'Endocrinologist'),
        ('GASTRO', 'Gastroenterologist'),
        ('URO', 'Urologist'),
        ('PULMO', 'Pulmonologist'),
        ('RAD', 'Radiologist'),
        ('ANESTH', 'Anesthesiologist'),
        ('PATH', 'Pathologist'),
        ('PLAST', 'Plastic Surgeon'),
        ('CHIRO', 'Chiropractor'),
    ]
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE , related_name='Doctor_profile')
    speciality = models.CharField(max_length=20 , choices=SPECIALITIES , default='GP')
    license_number = models.CharField(max_length=50, unique=True , null=True)
    room_number = models.CharField(max_length=10 ,null=True)
    qualifications = models.TextField(null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    languages_spoken = models.CharField(max_length=200 ,null=True)
    phone = models.CharField(max_length=15 ,null=True)
    emergency_contact = models.CharField(max_length=15 ,null=True)
    is_available = models.BooleanField(default=True ,null=True)
    image = models.ImageField(null=True, upload_to=Doctor_image_file_path)


    def __str__(self):
        return f"{self.user.username}'s Doctor Profile"
    
    
    
class Receptionist(models.Model):
    SHIFTS=(
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
        ('Night', 'Night')
    )
    user = models.OneToOneField(CustomUser ,on_delete=models.CASCADE , related_name='Receptionist_name')
    department = models.CharField(max_length=100, blank=True, null=True)
    shift = models.CharField(max_length=50, choices=SHIFTS ,null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    languages_spoken = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=15 ,null=True)
    emergency_contact = models.CharField(max_length=15 ,null=True)
    is_available = models.BooleanField(default=True ,null=True)

    def __str__(self):
        return f"{self.user.username}'s Receptionist Profile"


    
class Patient(models.Model):
    user = models.OneToOneField(CustomUser ,on_delete=models.CASCADE , related_name='Patient_name')
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=15 , null=True)
    emergency_contact = models.CharField(max_length=15 , null=True)
    
    
    def __str__(self):
        return f"{self.user.username}'s Patient Profile"
    

class Booking(models.Model):
    
    STATUS=(
        ('pending' , 'Pending'),
        ('accepted','Accepted'),
        ('rejected','Rejected'),
    )
    
    
    patient= models.ForeignKey(Patient , on_delete= models.CASCADE  , related_name='Patient_booked')
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE , related_name= "Doctor_booked")
    created_at = models.DateField(auto_now_add=True)
    reason = models.TextField()
    status = models.CharField(max_length=20 , choices=STATUS , default='pending')
    receptionist = models.ForeignKey(Receptionist, on_delete=models.CASCADE, related_name='receptionist_reviewed', blank=True, null=True)
    appointment_date = models.DateField(null=True, blank=True)
    appointment_time = models.TimeField(null=True, blank=True)
    appointment_details = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return f"Booking by {self.patient.user.username} with {self.doctor.user.username} - {self.status}"
    
    
    

