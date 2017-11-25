from django.db import models
from django.contrib import admin


class ArchitecturalNeeds(models.Model):
    environment_relationship = models.BooleanField(default=False, verbose_name=u'Texto/Planilha da Relação de Ambientes')
    functional_organogram = models.BooleanField(default=False, verbose_name=u'Organograma Funcional')
    project= models.ForeignKey('Project', blank=True, null=True)


    class Meta:
        abstract = False
        verbose_name_plural = "Programa de Necessidades de Arquitetura"
        verbose_name = "Programa de Necessidades de Arquitetura"

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('id', 'environment_relationship', 'functional_organogram', )