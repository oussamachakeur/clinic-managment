from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patient_view.views import BookingVS

router = DefaultRouter()
router.register(r'book', BookingVS, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
