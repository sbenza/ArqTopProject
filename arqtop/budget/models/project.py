from django.db import models
from django.contrib import admin

PROJECT_TYPE_CHOICES = (('EXP', 'Expansão'), ('INR', 'Reforma Interna'), ('NCO', 'Nova Contrução'),)
PROJECT_SCALE_CHOICES = (('SML', 'Pequeno'), ('MED', 'Médio'), ( 'BIG', 'Grande'),)
PROJECT_COMPLEXITY_CHOICE = (('LOW', 'Baixa'),('MED', 'Média'), ('HIG', 'Alta'),)


class Project(models.Model):
    date = models.DateTimeField(verbose_name='Data')
    project_type = models.CharField(max_length=3, choices=PROJECT_TYPE_CHOICES, default='INR', verbose_name='Tipo do Projeto')
    project_scale = models.CharField(max_length=3, choices=PROJECT_SCALE_CHOICES, default='MED', verbose_name='Escala do Projeto')
    project_complexity = models.CharField(max_length=3, choices=PROJECT_COMPLEXITY_CHOICE, default='MED', verbose_name='Complexidade do Projeto')
    legal_project = models.BooleanField(default=False, verbose_name=u'Projeto Legal')
    #discount_surcharge = models.FloatField(verbose_name='Desconto ou Acréscimo', blank=True, null=True)

    class Meta:
        abstract = False
        verbose_name_plural = "Projetos"
        verbose_name = "Projeto"

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class DataEntryInlineAdmin(admin.StackedInline):
    from .data_entry import DataEntry
    model = DataEntry
    extra = 1


class ArchitecturalNeedsInlineAdmin(admin.StackedInline):
    from .architectural_needs import ArchitecturalNeeds
    model = ArchitecturalNeeds
    extra = 1


class ExecutiveProjectInlineAdmin(admin.StackedInline):
    from .executive_project import ExecutiveProject
    model = ExecutiveProject
    extra = 1


class PreliminaryStudyInlineAdmin(admin.StackedInline):
    from .preliminary_study import PreliminaryStudy
    model = PreliminaryStudy
    extra = 1


class ClientInlineAdmin(admin.StackedInline):
    from .client import Client
    model = Client
    extra = 1


class Admin(admin.ModelAdmin):
    list_display = ('id', 'project_type', 'project_scale', 'project_complexity',
                     'legal_project', )
    inlines = (DataEntryInlineAdmin, ArchitecturalNeedsInlineAdmin, ExecutiveProjectInlineAdmin, PreliminaryStudyInlineAdmin, ClientInlineAdmin )