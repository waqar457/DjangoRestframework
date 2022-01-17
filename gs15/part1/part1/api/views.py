from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView, ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView




class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    
class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers    

class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers    

class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers    
