from .models import History
from rest_framework import viewsets
from .serializers import HistorySerializer


class HistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = History.objects.all()
    serializer_class = HistorySerializer
