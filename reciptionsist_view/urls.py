from django.urls import path, include
from reciptionsist_view.views import BookingList , BookingManageVS



urlpatterns = [
    path('dashboard/' , BookingList.as_view() , name='reciptionDashboard'),
    path('dashboard/<int:pk>' , BookingManageVS.as_view() , name='patientdetail'),
]
