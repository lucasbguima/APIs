from rest_framework import serializers
from .models import User, Agendamento, Hotel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'endereco', 'rg', 'cpf', 'telefone')

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ('cliente', 'hotel', 'status', 'data_inicio', 'data_termino')

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('nome', 'localidade', 'email')