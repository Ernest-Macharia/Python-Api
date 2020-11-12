from rest_framework import viewsets
from . import models
from .serializers import NoteSerializer




class NoteViewSet(viewsets.ModelViewSet):
    queryset = models.Noting.objects.all()
    serializer_class = NoteSerializer






