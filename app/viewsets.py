# views.py
from rest_framework import viewsets
from .models import AITool
from .serializers import AIToolSerializer

class AIToolViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `list`, `create`, `retrieve`, `update`, and `destroy` actions
    for the AITool model.
    """
    queryset = AITool.objects.all()
    serializer_class = AIToolSerializer
