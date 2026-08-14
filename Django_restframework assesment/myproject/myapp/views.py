from django.shortcuts import render
from myapp.models import *
from rest_framework import viewsets
from django.db import transaction
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()

# Create your views here.
def index(request):
    return render(request,"index.html")

