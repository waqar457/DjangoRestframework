from functools import partial
from django.shortcuts import render
from api import serializers
from api.models import Student
from api.serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class StudentAPI(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializers(stu,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete data updated"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializers(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial data updated"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data Deleted"})    
