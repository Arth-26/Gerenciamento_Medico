from rest_framework import serializers
from gerenciamento.models import *
from gerenciamento.validators import *


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'last_name', 'email', 'password']
    

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    Consulta = ConsultaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Medico
        fields = '__all__'
        
class PacienteSerializer(serializers.ModelSerializer):
   Consulta = ConsultaSerializer(many=True, read_only=True)
   
   class Meta:
       model = Paciente
       fields = '__all__'
       
class EnderecoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Endereco
        fields = '__all__'
        
class CoordenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenador
        fields = '__all__'
        

       