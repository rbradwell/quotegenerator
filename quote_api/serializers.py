from rest_framework import serializers
from .models import ActorQuote

class ActorQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorQuote
        fields = ['id','actor', 'quote','title', 'image']