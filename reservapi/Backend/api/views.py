from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Agendamento, Hotel
from .serializers import UserSerializer, AgendamentoSerializer, HotelSerializer

# Views API

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer