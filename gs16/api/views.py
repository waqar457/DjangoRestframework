from functools import partial
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all()
        serializer=StudentSerializers(stu,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        id=pk    
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu)
            return Response(serializer.data)
    def create(self,request):
        serializer=StudentSerializers(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializers(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data Complete update"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Update"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    def destroy(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()        
        return Response({"msg":"Data Deleted"})


