from main.models import Bet,BetStatus, Manager
from rest_framework import serializers


class BetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bet
        fields = ('id', 'first_side', 'second_side', 'first_side_bet', 'second_side_bet', 'title', 'note',
                  'status', 'result', 'created_at', 'updated_at'
        )


class BetStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BetStatus
        fields = ('id', 'name')


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('id', 'first_name', 'last_name', 'telegram_slug', 'engine_id', 'created_at', 'updated_at')