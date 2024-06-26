# Generated by Django 5.0.1 on 2024-05-19 19:37

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import enumfields.fields
import gerenciamento.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('SEGUNDA', 'Segunda-feira'), ('TERCA', 'Terça-feira'), ('QUARTA', 'Quarta-feira'), ('QUINTA', 'Quinta-feira'), ('SEXTA', 'Sexta-feira'), ('SABADO', 'Sábado'), ('DOMINGO', 'Domingo')], max_length=40)),
                ('data', models.DateField()),
                ('horario_inicio', models.TimeField()),
                ('horario_fim', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('dia', models.CharField(max_length=40)),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(blank=True, max_length=9, null=True)),
                ('pais', models.CharField(max_length=255)),
                ('estado', enumfields.fields.EnumField(enum=gerenciamento.models.EstadoEnum, max_length=2)),
                ('cidade', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('rua', models.CharField(max_length=40)),
                ('numero_casa', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm_estado', enumfields.fields.EnumField(enum=gerenciamento.models.EstadoEnum, max_length=2)),
                ('crm_digito', models.CharField(max_length=6)),
                ('especialidade', models.CharField(max_length=255)),
                ('nome_completo', models.CharField(max_length=255)),
                ('agenda', models.ManyToManyField(related_name='horario_medico', to='gerenciamento.agenda')),
                ('consulta', models.ManyToManyField(related_name='consulta_medico', to='gerenciamento.consulta')),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medico_consulta', to='gerenciamento.medico', verbose_name='medico_consulta'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medico_horario', to='gerenciamento.medico'),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=255)),
                ('codigo_sus', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('data_nasc', models.DateField()),
                ('telefone', models.CharField(max_length=255, unique=True)),
                ('consulta', models.ManyToManyField(related_name='consulta_paciente', to='gerenciamento.consulta')),
                ('endereco', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='endereco_paciente', to='gerenciamento.endereco')),
            ],
        ),
        migrations.AddField(
            model_name='endereco',
            name='paciente',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='endereco_paciente', to='gerenciamento.paciente'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_consulta', to='gerenciamento.paciente', verbose_name='paciente_consulta'),
        ),
    ]
