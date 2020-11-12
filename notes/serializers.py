from rest_framework import serializers
from .models import Noting

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noting
        fields = '__all__'
