from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import NoteSerializer
from .models import Noting
from rest_framework import status
# Create your views here.


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_notes(request):
    
    notes = Noting.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return JsonResponse({'notes': serializer.data}, safe=False, status=status.HTTP_200_OK)
