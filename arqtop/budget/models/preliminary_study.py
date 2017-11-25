from django.db import models
from django.contrib import admin


class PreliminaryStudy(models.Model):
    general_site_plan= models.BooleanField(default=False, verbose_name=u'Planta Geral de Implementação')
    preliminary_study_desing = models.BooleanField(default=False, verbose_name=u'Desenhos EP: Plantas, Cortes e Elevação')
    external_perspectives = models.BooleanField(default=False, verbose_name=u'Perspectivas Externas')
    internal_perspectives = models.BooleanField(default=False, verbose_name=u'Perspectivas Internas')
    project = models.ForeignKey('Project', blank=True, null=True)


    class Meta:
        abstract = False
        verbose_name_plural = "Estudos Preliminares"
        verbose_name = "Estudo Preliminar"

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('id', 'general_site_plan', 'preliminary_study_desing','external_perspectives',
                    'internal_perspectives',)