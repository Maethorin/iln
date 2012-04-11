#!/usr/bin/env python
# encoding: utf-8

from website.models import Premio, Categoria, Tarefa, GrupoDeTarefas
from django.contrib import admin

class PremioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}

class GrupoDeTarefasAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}

admin.site.register(Premio, PremioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(GrupoDeTarefas,GrupoDeTarefasAdmin)
admin.site.register(Tarefa)