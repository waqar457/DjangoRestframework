from django.shortcuts import render
from rest_framework import serializers
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

# MOdel Object - Single Student Data

def student_detial(request,pk):
    stu=Student.objects.get(id=pk)    # complex data
    serializer=StudentSerializer(stu) # convert into python native data type (dict)
    # json_data=JSONRenderer().render(serializer.data) # Render into json string
    # return HttpResponse(json_data,content_type='application/json')

    return JsonResponse(serializer.data,safe=False)

def student_list(request):
    stu=Student.objects.all()    # complex data
    serializer=StudentSerializer(stu,many=True) # convert into python native data type (dict)
    json_data=JSONRenderer().render(serializer.data) # Render into json string

    return HttpResponse(json_data,content_type='application/json')
