from django.db import models
from rest_framework import serializers
from .models import Task

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields= '__all__'