from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ...models import Coordenador, Paciente
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

# Teste de integração coordenador
class CoordenadorViewSetIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_url = reverse('Coordenadores-list')
        self.coordenador_data = {
            'nome': 'Teste',
            'sobrenome': 'Coordenador',
            'email': 'coordenador@example.com',
            'password': 'testpassword',
            'telefone': '123456789',
        }

        # Criando um coordenador para testar
        self.coordenador = Coordenador.objects.create(**self.coordenador_data)

        # Gerando um token JWT para o coordenador
        refresh = RefreshToken.for_user(self.coordenador)
        self.access_token = str(refresh.access_token)

    def test_create_coordenador_integration(self):
        # Autenticando o cliente com o token JWT do coordenador
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        response = self.client.post(self.create_url, self.coordenador_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('Coordenador criado com sucesso.' in response.data)
        
        # Verifica se o coordenador foi criado no banco de dados
        self.assertTrue(Coordenador.objects.filter(email=self.coordenador_data['email']).exists())

# Teste de integração paciente
class PacienteViewSetIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_url = reverse('Pacientes-list')
        self.paciente_data = {
            "nome": "test",
            "sobrenome": "testes",
            "cpf": "12312312345",
            "codigo_sus": "13231",
            "email": "teste@testes.com",
            "password": "123456",
            "data_nasc": "1999-01-01",
            "telefone": "123456612"
        }

    def test_create_paciente_integration(self):
        grupo, _ = Group.objects.get_or_create(name='role_paciente')
        paciente = Paciente.objects.create(**self.paciente_data)
        self.client.force_authenticate(user=paciente)
        response = self.client.post(self.create_url, self.paciente_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('Paciente criado com sucesso.' in response.data)

        # Verifica se o paciente foi criado no banco de dados
        self.assertTrue(Paciente.objects.filter(email=self.paciente_data['email']).exists())