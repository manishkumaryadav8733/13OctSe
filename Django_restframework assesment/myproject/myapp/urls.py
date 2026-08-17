from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
