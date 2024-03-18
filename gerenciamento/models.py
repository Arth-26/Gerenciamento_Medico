from django.db import models
from enumfields import EnumField

class Paciente(models.Model):
    nome_completo = models.CharField(max_digits = 255, null = False, blank = False)
    cpf = models.CharField(max_digits = 255, null = False, blank = False)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)
    senha = models.CharField(max_length=255, blank=False, null=False)
    data_nasc = models.DateField()
    telefone = models.CharField(max_digits = 255, unique=True, null = False, blank = False)
    endereco = models.OneToOneField('Endereco', on_delete=models.SET_NULL, blank=True, null = True)

class EstadoEnum(models.TextChoices):
    ACRE = 'AC', 'Acre'
    ALAGOAS = 'AL', 'Alagoas'
    AMAPA = 'AP', 'Amapá'
    AMAZONAS = 'AM', 'Amazonas'
    BAHIA = 'BA', 'Bahia'
    CEARA = 'CE', 'Ceará'
    DISTRITO_FEDERAL = 'DF', 'Distrito Federal'
    ESPIRITO_SANTO = 'ES', 'Espírito Santo'
    GOIAS = 'GO', 'Goiás'
    MARANHAO = 'MA', 'Maranhão'
    MATO_GROSSO = 'MT', 'Mato Grosso'
    MATO_GROSSO_DO_SUL = 'MS', 'Mato Grosso do Sul'
    MINAS_GERAIS = 'MG', 'Minas Gerais'
    PARA = 'PA', 'Pará'
    PARAIBA = 'PB', 'Paraíba'
    PARANA = 'PR', 'Paraná'
    PERNAMBUCO = 'PE', 'Pernambuco'
    PIAUI = 'PI', 'Piauí'
    RIO_DE_JANEIRO = 'RJ', 'Rio de Janeiro'
    RIO_GRANDE_DO_NORTE = 'RN', 'Rio Grande do Norte'
    RIO_GRANDE_DO_SUL = 'RS', 'Rio Grande do Sul'
    RONDONIA = 'RO', 'Rondônia'
    RORAIMA = 'RR', 'Roraima'
    SANTA_CATARINA = 'SC', 'Santa Catarina'
    SAO_PAULO = 'SP', 'São Paulo'
    SERGIPE = 'SE', 'Sergipe'
    TOCANTINS = 'TO', 'Tocantins'

class Endereco(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, related_name='endereco_paciente')
    cep = models.CharField(max_length=9, null=True, blank=True)
    pais = models.CharField(max_length=255, null=False, blank=False)
    estado = EnumField(EstadoEnum, max_length=2)
    cidade = models.CharField(max_length=255, null=False, blank=False)
    bairro = models.CharField(max_length=255, null=False, blank=False)
    rua = models.CharField(max_length=40, null=False, blank=False)
    numero_casa = models.IntegerField(null=True)