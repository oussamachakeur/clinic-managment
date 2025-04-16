from django.urls import path , include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView 
from users import views

router = DefaultRouter()
router.register(r'register' , views.UserRegistrationVS),



app_name = 'users'


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('doctors/' , views.DoctorsListVS.as_view() , name= 'doctorList'),
    path('doctors/<int:pk>' ,  views.DoctorProfileVS.as_view() , name='doctorProfile'),
    
    path('receptionists/' , views.ReceptionistListVS.as_view() , name='receptionistList'),
    path('receptionists/<int:pk>' , views.ReceptionisProfile.as_view() , name='receptionistsProfile'),
    
    path('patients/' , views.PatientListVS.as_view() , name='patientsList'),
    path('patients/<int:pk>' , views.PatientProfilesVS.as_view() , name='patientsProfile')
]
