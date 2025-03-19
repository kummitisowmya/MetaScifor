from django.shortcuts import render
from rest_framework import viewsets
from apiapp.serializers import *
from apiapp.models import *
# Create your views here.
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer