#!/usr/bin/env python
# encoding: utf-8

from website.models import Premio, Categoria, Tarefa, GrupoDeTarefas, Sabor, Cor, Tamanho, Conta, Resgate, MovimentacaoDeConta
from django.contrib import admin

class AdminComSlug(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}

class PremioAdmin(AdminComSlug):
    pass

class CategoriaAdmin(AdminComSlug):
    pass

class GrupoDeTarefasAdmin(AdminComSlug):
    pass

admin.site.register(Premio, PremioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(GrupoDeTarefas,GrupoDeTarefasAdmin)

admin.site.register(Conta)
admin.site.register(Tarefa)
admin.site.register(Sabor)
admin.site.register(Cor)
admin.site.register(Tamanho)


#TODO: queime depois de ler
admin.site.register(Resgate)
admin.site.register(MovimentacaoDeConta)
