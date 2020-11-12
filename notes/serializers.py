from rest_framework import serializers
from .models import Noting

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noting
        fields = ['note', 'created_at']
