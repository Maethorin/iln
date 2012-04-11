#!/usr/bin/env python
# encoding: utf-8
from django.contrib.auth.models import User

from django.db import models

class Conta(models.Model):
    usuario = models.ForeignKey(User, unique=True)
    numero = models.IntegerField('Número', default=0, unique=True)
    saldo = models.IntegerField("Saldo", default=0)
    premios_recuperados = models.ManyToManyField("Premio")

    def __unicode__(self):
        return 'Usuário %s tem $ILN %s,00 de saldo' % (self.usuario.first_name, self.saldo)

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=120, default='', unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
        return self.nome

class Premio(models.Model):
    nome = models.CharField('Nome', max_length=120, default='', unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    valor = models.IntegerField('Valor', default=0)
    prazo_de_entrega = models.IntegerField('Prazo de entrega (dias)', default=1)
    descricao = models.CharField("Descrição", max_length=300, blank=True)
    thumbnail = models.CharField("Thumbnail", max_length=300, blank=True)
    quantidade_de_fotos = models.IntegerField("Quantidade de Fotos", default=0)
    mais_informacoes = models.CharField("Mais Informações", max_length=300, blank=True)
    categoria = models.ForeignKey("Categoria", null=True)

    def obter_classe_da_coluna(self):
        if self.quantidade_de_fotos == 2:
            return "sixcol"
        if self.quantidade_de_fotos == 3:
            return "fourcol"
        if self.quantidade_de_fotos == 4:
            return "threecol"
        return ""

    def obter_fotos(self):
        nome = self.thumbnail.replace(".jpg", "")
        if self.quantidade_de_fotos == 1:
            return "%s-1.jpg" % nome

        fotos = []
        for i in range(1, self.quantidade_de_fotos + 1):
            fotos.append("%s-%s.jpg" % (nome, i))
        return fotos

    def __unicode__(self):
        return "%s custa ILN$ %s,00 e entrega em %s dia(s)" % (self.nome, self.valor, self.prazo_de_entrega)

class GrupoDeTarefas(models.Model):
    nome = models.CharField('Nome', max_length=120, default='', unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def tarefas(self):
        return self.tarefa_set.all()

    def __unicode__(self):
        return self.nome


class Tarefa(models.Model):
    nome = models.CharField('Nome', max_length=120)
    valor = models.IntegerField('Valor', default=0)
    tempo_para_execucao = models.IntegerField('Tempo para execução (minutos)', default=0, blank=True)
    bonus_voluntario = models.IntegerField('Bônus para voluntário', default=0, blank=True)
    tempo_para_bonus = models.IntegerField('Tempo para bônus de antecipação', default=0, blank=True)
    bonus_de_tempo = models.IntegerField('Bônus para completar antes do tempo', default=0, blank=True)
    tempo_para_desconto = models.IntegerField('Tempo para desconto', default=0, blank=True)
    desconto_por_tempo = models.IntegerField('Desconto por tempo', default=0, blank=True)
    tempo_limite = models.IntegerField('Tempo limite', default=0, blank=True)
    grupo = models.ForeignKey('GrupoDeTarefas', null=True)

    def __unicode__(self):
        return "%s/%s - ganha $ILN %s,00" % (self.grupo.nome, self.nome, self.valor)
