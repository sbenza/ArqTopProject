from django.db import models
from django.contrib import admin


class ExecutiveProject(models.Model):
    electrical_plant= models.BooleanField(default=False, verbose_name=u'Planta de Pontos Elétricos e Iluminação')
    executive_project_desing = models.BooleanField(default=False, verbose_name=u'Desenhos PE: Plantas, Cortes e Elevação')
    humanized_plant = models.BooleanField(default=False, verbose_name=u'Planta Humanizada com Layout Proposto')
    inverted_floor_plant = models.BooleanField(default=False, verbose_name=u'Planta Invertida de Forro')
    coating_indication_plant = models.BooleanField(default=False, verbose_name=u'Planta de Indicação de Revestimento')
    structural_elements_plant = models.BooleanField(default=False, verbose_name=u'Planta de Elementos Estructurais')
    hidraulic_plant = models.BooleanField(default=False, verbose_name=u'Planta de Pontos Hidráulicos')


    class Meta:
        abstract = False
        verbose_name_plural = "Projeto Executivo"
        verbose_name = "Projeto Executivo"

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('id', 'electrical_plant', 'executive_project_desing','humanized_plant', 'inverted_floor_plant',
                    'coating_indication_plant', 'structural_elements_plant', 'hidraulic_plant',)