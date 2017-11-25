from django.db import models
from django.contrib import admin


class DataEntry(models.Model):
    site_measurement = models.BooleanField(default=False, verbose_name=u'Medição do Local')
    photographic_report = models.BooleanField(default=False, verbose_name=u'Relatório Fotográfico')
    textual_report = models.BooleanField(default=False,verbose_name=u'Relatório Textual')
    current_situation_blueprint = models.BooleanField(default=False, verbose_name=u'Desenho Técnico da Situação Atual do Local (Plantas e Cortes)')

    class Meta:
        abstract = False
        verbose_name_plural = "Levantamento de Dados"
        verbose_name = "Levantamento de Dados"

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('id', 'site_measurement', 'photographic_report', 'current_situation_blueprint', 'textual_report', )