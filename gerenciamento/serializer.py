from rest_framework import serializers
from gerenciamento.models import *
from gerenciamento.validators import *

class ConsultaSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = Consulta
        fields = "__all__"

class MedicoSerializer(serializers.ModelSerializer):
    Consulta = ConsultaSerializer(many=True, read_only=True)
    
    class Meta:
        models = Medico
        fields = "__all__"
        
class PacienteSerializer(serializers.ModelSerializer):
   Consulta = ConsultaSerializer(many=True, read_only=True)
   
   class Meta:
       models = Paciente
       fields = ['cpf', 'email', 'data_nasc', 'nome_completo', 'telefone', 'endereco']
       
class EnderecoSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = Endereco
        fields = "__all__"

class ModeradorSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = Moderador
        fields = "__all__"
        
class CoordenadorSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = Coordenador
        fields = "__all__"
        

       