#!/usr/bin/env python
# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save

class Conta(models.Model):
    usuario = models.OneToOneField(User, unique=True)
    numero = models.IntegerField('Número', default=0, unique=True)
    saldo = models.IntegerField("Saldo", default=0)
    premios_resgatados = models.ManyToManyField("Premio", through='Resgate', null=True, blank=True)

    def __unicode__(self):
        return u'Usuário %s tem $ILN %s,00 de saldo' % (self.usuario.first_name, self.saldo)

class MovimentacaoDeConta(models.Model):
    conta = models.ForeignKey('Conta')
    valor = models.IntegerField("Valor", default=0)
    data = models.DateTimeField(u"Data hora da movimentação")
    tipo = models.CharField(u'Tipo da movimentação', max_length=1, choices=(('R', 'Resgate'),('T', 'Tarefa')))
    resgate = models.ForeignKey('Resgate', null=True, blank=True, default=None)
    tarefa = models.ForeignKey('Tarefa', null=True, blank=True, default=None)
    saldo = models.IntegerField("Saldo", default=0)

    def descricao(self):
        if self.tipo == 'T':
            return self.tarefa.nome
        return self.resgate.premio.nome

    def __unicode__(self):
        if self.tipo == 'T':
            return "%s ganhou %s por ter realizado %s em %s" % (
                self.conta.usuario.first_name,
                self.valor,
                self.tarefa.nome,
                self.data.strftime("%d/%m/%Y %H:%M")
            )

        return "%s gastou %s resgatando %s %s em %s" % (
            self.conta.usuario.first_name,
            self.valor,
            self.resgate.quantidade,
            self.resgate.premio.nome,
            self.data.strftime("%d/%m/%Y %H:%M")
        )

def atualiza_saldo_da_movimentacao(sender, instance, **kwargs):
    movimentacoes_da_conta = MovimentacaoDeConta.objects.filter(conta=instance.conta)
    saldo = 0
    valor = instance.valor
    if instance.tipo == 'R':
        valor *= -1
    if movimentacoes_da_conta.exists():
        saldo = movimentacoes_da_conta.latest('data').saldo

    saldo += valor
    instance.saldo = saldo

def atualiza_saldo_da_conta(sender, instance, **kwargs):
    instance.conta.saldo = instance.saldo
    instance.conta.save()

pre_save.connect(atualiza_saldo_da_movimentacao, sender=MovimentacaoDeConta)
post_save.connect(atualiza_saldo_da_conta, sender=MovimentacaoDeConta)

class Resgate(models.Model):
    conta = models.ForeignKey('Conta')
    premio = models.ForeignKey('Premio')
    quantidade = models.IntegerField('Quantidade', default=0)
    data = models.DateTimeField("Data hora do resgate")

    def __unicode__(self):
        return u"%s resgatou %s %s em %s" % (
            self.conta.usuario.first_name,
            self.quantidade,
            self.premio.nome,
            self.data.strftime("%d/%m/%Y %H:%M")
        )

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=120, default='', unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
        return self.nome

class Sabor(models.Model):
    class Meta:
        verbose_name = "Sabor"
        verbose_name_plural = "Sabores"
        ordering = ('nome',)

    nome = models.CharField('Nome', max_length=120, default='', unique=True)

    def __unicode__(self):
        return self.nome

class Cor(models.Model):
    class Meta:
        verbose_name = "Cor"
        verbose_name_plural = "Cores"
        ordering = ('nome',)

    nome = models.CharField('Nome', max_length=120, default='', unique=True)
    hexa = models.CharField('Código hexa (sem o #)', max_length=6, default='000')

    def __unicode__(self):
        return self.nome

class Tamanho(models.Model):
    class Meta:
        verbose_name = "Tamanho"
        verbose_name_plural = "Tamanhos"
        ordering = ('nome',)

    nome = models.CharField('Nome', max_length=120, default='', unique=True)
    abreviatura = models.CharField('Abreviatura', max_length=3, default='')

    def __unicode__(self):
        if self.abreviatura:
            return self.abreviatura
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
    sabores = models.ManyToManyField('Sabor', null=True, blank=True)
    cores = models.ManyToManyField('Cor', null=True, blank=True)
    tamanhos = models.ManyToManyField('Tamanho', null=True, blank=True)

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

    def tem_sabores(self):
        return self.sabores.count() > 0

    def tem_cores(self):
        return self.cores.count() > 0

    def __unicode__(self):
        return u"%s custa ILN$ %s,00 e entrega em %s dia(s)" % (self.nome, self.valor, self.prazo_de_entrega)

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
    vountario = models.ForeignKey('Conta', null=True, blank=True, default=None)

    def __unicode__(self):
        return u"%s/%s - ganha $ILN %s,00" % (self.grupo.nome, self.nome, self.valor)
