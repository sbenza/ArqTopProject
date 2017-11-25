from django.db import models
from django.contrib import admin

PROJECT_TYPE_CHOICES = (('EXP', 'Expansão'), ('INR', 'Reforma Interna'), ('NCO', 'Nova Contrução'),)
PROJECT_SCALE_CHOICES = (('SML', 'Pequeno'), ('MED', 'Médio'), ( 'BIG', 'Grande'),)
PROJECT_COMPLEXITY_CHOICE = (('LOW', 'Baixa'),('MED', 'Média'), ('HIG', 'Alta'),)


class Project(models.Model):
    date=models.DateTimeField(verbose_name='Data')
    project_type = models.CharField(max_length=3, choices=PROJECT_TYPE_CHOICES, default='INR', verbose_name='Tipo do Projeto')
    project_scale = models.CharField(max_length=3, choices=PROJECT_SCALE_CHOICES, default='MED', verbose_name='Escala do Projeto')
    project_complexity = models.CharField(max_length=3, choices=PROJECT_COMPLEXITY_CHOICE, default='MED', verbose_name='Complexidade do Projeto')
    data_entry=  models.ForeignKey('DataEntry', blank=True, null=True,)
    architectural_needs= models.ForeignKey('ArchitecturalNeeds', blank=True, null=True)
    preliminary_study=models.ForeignKey('PreliminaryStudy', blank=True, null=True)
    executive_project= models.ForeignKey('ExecutiveProject', blank=True, null=True)
    legal_project = models.BooleanField(default=False, verbose_name=u'Projeto Legal')
    discount_surcharge = models.FloatField(verbose_name='Desconto ou Acréscimo', blank=True, null=True)


    class Meta:
        abstract = False
        verbose_name_plural = "Projetos"
        verbose_name = "Projeto"

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('id', 'project_type', 'project_scale', 'project_complexity', 'data_entry','architectural_needs',
                    'preliminary_study', 'executive_project', 'legal_project','discount_surcharge', 'date', )