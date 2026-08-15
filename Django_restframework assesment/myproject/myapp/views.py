from django.shortcuts import render
from myapp.models import *
from rest_framework import viewsets,filters
from django.db import transaction
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    serializer_class = DoctorSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'specialization']



    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()

# Create your views here.
def index(request):
    return render(request,"index.html")

