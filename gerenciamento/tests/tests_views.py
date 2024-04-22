from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Coordenador, Paciente, Endereco



class CoordenadorViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)

    # Este teste verifica se um coordenador pode ser criado corretamente.
    def test_create_coordenador(self):
        data = {
            'nome': 'Teste',
            'sobrenome': 'Coordenador',
            'email': 'coordenador@example.com',
            'password': 'testpassword',
        }
        response = self.client.post('/coordenadores/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Coordenador.objects.count(), 1)

    # Este teste verifica se um coordenador pode ser excluído corretamente.
    def test_destroy_coordenador(self):
        coordenador = Coordenador.objects.create(nome='Teste', sobrenome='Coordenador', email='coordenador@example.com')
        response = self.client.delete(f'/coordenadores/{coordenador.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Coordenador.objects.count(), 0)


class PacienteViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)

    def test_create_paciente(self):
        data = {
            'nome': 'Teste',
            'sobrenome': 'Paciente',
            'cpf': '12345678900',  # Adicione um CPF válido
            'codigo_sus': '12345678900',  # Adicione um código SUS válido
            'email': 'paciente@example.com',
            'password': 'testpassword',
            'data_nasc': '2000-01-01',  # Adicione uma data de nascimento válida
            'telefone': '123456789',  # Adicione um telefone válido
            'endereco': {  # Adicione um endereço válido
                'cep': '12345678',
                'pais': 'Brasil',
                'estado': 'SP',
                'cidade': 'São Paulo',
                'bairro': 'Bairro',
                'rua': 'Rua',
                'numero_casa': 123
            }
        }
        response = self.client.post('/pacientes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Paciente.objects.count(), 1)

    def test_destroy_paciente(self):
        paciente = Paciente.objects.create(
            nome='Teste', sobrenome='Paciente', cpf='12345678900',
            codigo_sus='12345678900', email='paciente@example.com',
            password='testpassword', data_nasc='2000-01-01',
            telefone='123456789'
        )
        endereco_data = {
            'paciente': paciente,  # Adicionando o paciente ao objeto Endereco
            'cep': '12345678',
            'pais': 'Brasil',
            'estado': 'SP',
            'cidade': 'São Paulo',
            'bairro': 'Bairro',
            'rua': 'Rua',
            'numero_casa': 123
        }
        endereco = Endereco.objects.create(**endereco_data)
        paciente.endereco = endereco
        paciente.save()
        response = self.client.delete(f'/pacientes/{paciente.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Paciente.objects.count(), 0)