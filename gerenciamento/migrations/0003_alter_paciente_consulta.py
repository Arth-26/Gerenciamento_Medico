# Generated by Django 5.0.1 on 2024-05-19 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0002_alter_paciente_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='consulta',
            field=models.ManyToManyField(blank=True, null=True, related_name='consulta_paciente', to='gerenciamento.consulta'),
        ),
    ]
