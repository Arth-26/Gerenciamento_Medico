from django.contrib import admin
from .models import *

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'email')
    list_display_links = ('username', 'email')
    search_fields = ('username', 'email')
    list_per_page = 10

class Pacientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email' , 'cpf', 'data_nasc', 'telefone')
    list_display_links = ('id', 'nome', 'email')
    search_fields = ('nome', 'email')
    list_per_page = 10

class Medicos(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'crm_estado' , 'crm_digito', 'especialidade')
    list_display_links = ('id', 'nome_completo')
    search_fields = ( 'nome_completo', 'crm_estado' , 'crm_digito', 'especialidade')
    list_per_page = 10

class Coordenadores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone')
    list_display_links = ('id', 'nome', 'email')
    search_fields = ( 'nome', 'email')
    list_per_page = 10

class Consultas(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data', 'hora')
    list_display_links = ('paciente', 'medico', 'data', 'hora')
    search_fields = ('paciente', 'medico ', 'data', 'hora')
    list_per_page = 10

class Enderecos(admin.ModelAdmin):
    list_display = ('id', 'cep', 'pais', 'estado', 'cidade', 'bairro', 'rua', 'numero_casa', 'paciente')
    list_display_links = ('cep', 'id')
    search_fields = ('cep', 'id')
    list_per_page = 10
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Paciente, Pacientes)
admin.site.register(Medico, Medicos)
admin.site.register(Coordenador, Coordenadores)
admin.site.register(Consulta, Consultas)
admin.site.register(Endereco, Enderecos)