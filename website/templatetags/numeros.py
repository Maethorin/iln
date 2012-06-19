#!/usr/bin/env python
# encoding: utf-8

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='tempo')
def tempo(valor):
    horas = int(valor / 60)
    minutos = valor % 60

    return mark_safe('<span class="tempo">%sh %sm</span>' % (horas, minutos))

@register.filter(name='moeda')
def moeda(valor):
    return mark_safe('<span class="moeda">$ILN %s,00</span>' % valor)

@register.filter(name='moeda_simples')
def moeda_simples(valor):
    return mark_safe('<span class="moeda">%s,00</span>' % valor)

@register.filter(name='mod4')
def mod4(valor):
    return valor%4