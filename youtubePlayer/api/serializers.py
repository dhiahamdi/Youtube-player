from .models import History
from rest_framework import serializers


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'url', 'date']
