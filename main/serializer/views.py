from main.models import BetStatus, Bet, Manager
from rest_framework import viewsets
from main.serializers import BetSerializer, BetStatusSerializer, ManagerSerializer


class BetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Bet.objects.all().order_by('-updated_at')
    serializer_class = BetSerializer


class BetStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BetStatus.objects.all().order_by('-id')
    serializer_class = BetStatusSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Manager.objects.all().order_by('-updated_at')
    serializer_class = ManagerSerializer