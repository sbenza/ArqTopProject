from django.db import models
from django.contrib import admin


class Client(models.Model):
    name = models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    project = models.ForeignKey('Project', blank=True, null=True)
    class Meta:
        abstract = False
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"

    @classmethod
    def register_admin(cls):
        admin.site.register(cls, Admin)


class Admin(admin.ModelAdmin):
    list_display = ('id', 'name', )