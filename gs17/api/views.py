from functools import partial
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    querysets=Student.objects.all()
    Serializer_class=StudentSerializers()



