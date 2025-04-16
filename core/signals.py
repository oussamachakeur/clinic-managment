from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Doctor, Receptionist, Patient

@receiver(post_save, sender=CustomUser)
def create_profile_on_acceptance(sender, instance, created, **kwargs):
    # Only create profile if user is accepted
    if instance.status == 'accepted':
        if instance.role == 'doctor' and not hasattr(instance, 'Doctor_profile'):
            Doctor.objects.create(user=instance)
        elif instance.role == 'receptionist' and not hasattr(instance, 'Receptionist_name'):
            Receptionist.objects.create(user=instance)
        elif instance.role == 'patient' and not hasattr(instance, 'Patient_name'):
            Patient.objects.create(user=instance)
