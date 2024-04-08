from .models import Coordenador, Paciente, CustomUser
from .serializer import PacienteSerializer, CoordenadorSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated


class CoordenadorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Coordenadors"""
    queryset = Coordenador.objects.all()
    serializer_class = CoordenadorSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data

        # Serializar dados para Funcionario
        serializer_paciente = CoordenadorSerializer(data=data)
        if serializer_paciente.is_valid():
            coordenador = serializer_paciente.save()
        else:
            return Response(serializer_paciente.errors, status=status.HTTP_400_BAD_REQUEST)

        # Criar uma instância de OutraTabela com as informações necessárias
        user_data = {
            'username': data.get('nome'),
            'last_name': data.get('sobrenome'),
            'email': data.get('email'),
            'password': data.get('password'),

        }

        grupo, created = Group.objects.get_or_create(name='role_coordenador')

        User = get_user_model()
        user = User.objects.create_user(**user_data)
        
        user.groups.add(grupo)
        
        return Response("Coordenador criado com sucesso.", status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        
        try:
            user = CustomUser.objects.get(email=instance.email)
            user.delete()
        except CustomUser.DoesNotExist:
            pass

        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class PacienteViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Pacientes"""
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        # Serializar dados para Funcionario
        serializer_paciente = PacienteSerializer(data=data)
        if serializer_paciente.is_valid():
            paciente = serializer_paciente.save()
        else:
            return Response(serializer_paciente.errors, status=status.HTTP_400_BAD_REQUEST)

        # Criar uma instância de OutraTabela com as informações necessárias
        user_data = {
            'username': data.get('nome'),
            'last_name': data.get('sobrenome'),
            'email': data.get('email'),
            'password': data.get('password'),

        }

        grupo, created = Group.objects.get_or_create(name='role_paciente')

        User = get_user_model()
        user = User.objects.create_user(**user_data)
        
        user.groups.add(grupo)
        
        return Response("Paciente criado com sucesso.", status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        
        try:
            user = CustomUser.objects.get(email=instance.email)
            user.delete()
        except CustomUser.DoesNotExist:
            pass

        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

