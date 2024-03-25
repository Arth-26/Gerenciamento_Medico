from django.contrib import admin
from .models import *


@admin.register(Paciente)
class Pacientes(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'email' , 'cpf', 'data_nasc', 'telefone')
    list_display_links = ('id', 'nome_completo', 'email')
    search_fields = ('nome_completo', 'email')
    list_per_page = 10

@admin.register(Medico)
class Medicos(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'crm_estado' , 'crm_digito', 'especialidade')
    list_display_links = ('id', 'nome_completo')
    search_fields = ( 'nome_completo', 'crm_estado' , 'crm_digito', 'especialidade')
    list_per_page = 10
    
@admin.register(Coordenador)    
class Coordenadores(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'email', 'telefone')
    list_display_links = ('id', 'nome_completo', 'email')
    search_fields = ( 'nome_completo', 'email')
    list_per_page = 10
    
@admin.register(Moderador)
class Moderadores(admin.ModelAdmin):
    list_display = ('id', 'cpf', 'nome_completo', 'email', 'telefone')
    list_display_links = ('id', 'nome_completo', 'email')
    search_fields = ( 'nome_completo', 'email')
    list_per_page = 10
    
@admin.register(Consulta)
class Consultas(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data', 'hora')
    list_display_links = ('paciente', 'medico', 'data', 'hora')
    search_fields = ('paciente', 'medico ', 'data', 'hora')
    list_per_page = 10
    
@admin.register(Endereco)
class Enderecos(admin.ModelAdmin):
    list_display = ('id', 'cep', 'pais', 'estado', 'cidade', 'bairro', 'rua', 'numero_casa', 'paciente')
    list_display_links = ('cep', 'id')
    search_fields = ('cep', 'id')
    list_per_page = 10
    

