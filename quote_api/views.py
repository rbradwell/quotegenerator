from django.shortcuts import render
from rest_framework import viewsets
from .models import ActorQuote
from .serializers import ActorQuoteSerializer
# Create your views here.

class ActorQuoteViewSet(viewsets.ModelViewSet):
    queryset = ActorQuote.objects.all()
    serializer_class = ActorQuoteSerializer