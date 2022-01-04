from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer

# Create your views here.
@api_view(['GET',"POST","PUT","DELETE"])
def student_api(request,pk=None):
    if request.method=="GET":
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)    

    if request.method=="POST":
        ser=StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Data Created"})
        return Response(ser.errors)        

    if request.method=="PUT":
        id=pk
        stu=Student.objects.get(id=id)
        ser=StudentSerializer(stu,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Data Updated"})
        return Response(ser.errors)                

    if request.method=="DELETE":
        id=pk
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({"msg":"Data Deleted"})        