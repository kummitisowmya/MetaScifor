from apiapp.models import *
from rest_framework import serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'