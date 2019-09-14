from rest_framework import serializers
from server.apps.main import models

class HourSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'person',
            'clock_type',
            'time',
        )
        model = models.Hour
