# serializers.py
from rest_framework import serializers
from .models import AITool

class AIToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = AITool
        fields = ['id', 'name', 'description', 'website']  # always include 'id'
