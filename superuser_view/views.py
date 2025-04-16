from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Patient, Doctor, Receptionist
from django.db.models import Count

class AdminStatsView(APIView):
    def get(self, request):
        total_patients = Patient.objects.count()
        total_doctors = Doctor.objects.count()
        total_receptionists = Receptionist.objects.count()

        doctors_by_specialty = Doctor.objects.values('speciality').annotate(count=Count('id'))

        data = {
            'total_patients': total_patients,
            'total_doctors': total_doctors,
            'total_receptionists': total_receptionists,
            'doctors_by_specialty': list(doctors_by_specialty)
        }
        return Response(data)
