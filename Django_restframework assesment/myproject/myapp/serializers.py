from rest_framework import serializers
from myapp.models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
    def validate_name(self,value):
        if len(value)<3:
            raise serializers.ValidationError("name must have atleast 3 characters long")
        return value