from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import *
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasktable
        fields ='__all__'