from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import NoteSerializer
from .models import Noting
from rest_framework import status
import json
from rest_framework import generics
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.




class NoteCreateApi(generics.CreateAPIView):
    queryset = Noting.objects.all()
    serializer_class = NoteSerializer
    

class NoteListApi(generics.ListAPIView):
    queryset = Noting.objects.all()
    serializer_class = NoteSerializer