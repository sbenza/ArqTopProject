# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchitecturalNeeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_relationship', models.BooleanField(default=False, verbose_name='Texto/Planilha da Relação de Ambientes')),
                ('functional_organogram', models.BooleanField(default=False, verbose_name='Organograma Funcional')),
            ],
            options={
                'verbose_name': 'Programa de Necessidades de Arquitetura',
                'verbose_name_plural': 'Programa de Necessidades de Arquitetura',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_measurement', models.BooleanField(default=False, verbose_name='Medição do Local')),
                ('photographic_report', models.BooleanField(default=False, verbose_name='Relatório Fotográfico')),
                ('textual_report', models.BooleanField(default=False, verbose_name='Relatório Textual')),
                ('current_situation_blueprint', models.BooleanField(default=False, verbose_name='Desenho Técnico da Situação Atual do Local (Plantas e Cortes)')),
            ],
            options={
                'verbose_name': 'Levantamento de Dados',
                'verbose_name_plural': 'Levantamento de Dados',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExecutiveProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electrical_plant', models.BooleanField(default=False, verbose_name='Planta de Pontos Elétricos e Iluminação')),
                ('executive_project_desing', models.BooleanField(default=False, verbose_name='Desenhos PE: Plantas, Cortes e Elevação')),
                ('humanized_plant', models.BooleanField(default=False, verbose_name='Planta Humanizada com Layout Proposto')),
                ('inverted_floor_plant', models.BooleanField(default=False, verbose_name='Planta Invertida de Forro')),
                ('coating_indication_plant', models.BooleanField(default=False, verbose_name='Planta de Indicação de Revestimento')),
                ('structural_elements_plant', models.BooleanField(default=False, verbose_name='Planta de Elementos Estructurais')),
                ('hidraulic_plant', models.BooleanField(default=False, verbose_name='Planta de Pontos Hidráulicos')),
            ],
            options={
                'verbose_name': 'Projeto Executivo',
                'verbose_name_plural': 'Projeto Executivo',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreliminaryStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_site_plan', models.BooleanField(default=False, verbose_name='Planta Geral de Implementação')),
                ('preliminary_study_desing', models.BooleanField(default=False, verbose_name='Desenhos EP: Plantas, Cortes e Elevação')),
                ('external_perspectives', models.BooleanField(default=False, verbose_name='Perspectivas Externas')),
                ('internal_perspectives', models.BooleanField(default=False, verbose_name='Perspectivas Internas')),
            ],
            options={
                'verbose_name': 'Estudo Preliminar',
                'verbose_name_plural': 'Estudos Preliminares',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Data')),
                ('project_type', models.CharField(choices=[('EXP', 'Expansão'), ('INR', 'Reforma Interna'), ('NCO', 'Nova Contrução')], default='INR', max_length=3, verbose_name='Tipo do Projeto')),
                ('project_scale', models.CharField(choices=[('SML', 'Pequeno'), ('MED', 'Médio'), ('BIG', 'Grande')], default='MED', max_length=3, verbose_name='Escala do Projeto')),
                ('project_complexity', models.CharField(choices=[('LOW', 'Baixa'), ('MED', 'Média'), ('HIG', 'Alta')], default='MED', max_length=3, verbose_name='Complexidade do Projeto')),
                ('legal_project', models.BooleanField(default=False, verbose_name='Projeto Legal')),
                ('discount_surcharge', models.FloatField(blank=True, null=True, verbose_name='Desconto ou Acréscimo')),
                ('architectural_needs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.ArchitecturalNeeds')),
                ('data_entry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.DataEntry')),
                ('executive_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.ExecutiveProject')),
                ('preliminary_study', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.PreliminaryStudy')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
                'abstract': False,
            },
        ),
    ]
