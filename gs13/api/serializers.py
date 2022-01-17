from rest_framework import fields, serializers
from api.models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']