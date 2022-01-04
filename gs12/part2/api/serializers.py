from django.db import models
from django.db.models import fields
from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        # fields=["id","name","roll","city"]
        fields="__all__"