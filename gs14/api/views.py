# GenericAPIView and Model mixin

from rest_framework import serializers
from .models import Student
from api.serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class StudentList(ListModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreate(CreateModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentRetrive(RetrieveModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class StudentUpdate(UpdateModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class StudentDestroy(DestroyModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
