# urls.py
from django.urls import path, include
from rest_framework import routers
from .viewsets import AIToolViewSet

router = routers.DefaultRouter()
router.register(r'ai-tools', AIToolViewSet, basename='aitool')