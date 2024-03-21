from django.contrib import admin
from .models import *


class Pacientes(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'email' , 'cpf', 'data_nasc', 'telefone')
    list_display_links = ('id', 'nome_completo', 'email')
    search_fields = ('nome_completo', 'email')
    list_per_page = 10
    
class Medicos(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'crm_estado' , 'crm_digito', 'especialidade')
    list_display_links = ('id', 'nome_completo')
    search_fields = ( 'nome_completo', 'crm_estado' , 'crm_digito', 'especialidade')
    list_per_page = 10
    
class Coordenadores(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'email', 'telefone')
    list_display_links = ('id', 'nome_completo', 'email')
    search_fields = ( 'nome_completo', 'email')
    list_per_page = 10
    
class Moderadores(admin.ModelAdmin):
    list_display = ('id', 'cpf ', 'nome_completo', 'email', 'telefone')
    list_display_links = ('id', 'nome_completo', 'email')
    search_fields = ( 'nome_completo', 'email')
    list_per_page = 10
    
class Consultas(admin.ModelAdmin):
    list_display = ('paciente', 'medico ', 'data', 'hora')
    list_display_links = ('paciente', 'medico ', 'data', 'hora')
    search_fields = ('paciente', 'medico ', 'data', 'hora')
    list_per_page = 10
    
class Enderecos(admin.ModelAdmin):
    list_display = ('id', 'cep ', 'pais', 'estado', 'cidade', 'bairro', 'rua', 'numero_casa', 'paciente')
    list_display_links = ('cep', 'id')
    search_fields = ('cep', 'id')
    list_per_page = 10
    
    
admin.site.register(Pacientes,  Paciente)
admin.site.register(Medicos, Medico)
admin.site.register(Coordenadores, Coordenador)
admin.site.register(Moderadores, Moderador)
admin.site.register(Consultas, Consulta)
admin.site.register(Enderecos, Endereco)
