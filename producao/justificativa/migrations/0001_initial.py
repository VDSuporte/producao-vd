# Generated by Django 5.0.6 on 2024-07-10 11:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Justificativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição')),
                ('status', models.CharField(default='Pendente', max_length=150, verbose_name='Status')),
                ('data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data/Hora')),
            ],
        ),
    ]
