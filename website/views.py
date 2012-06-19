#!/usr/bin/env python
# encoding: utf-8
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic.simple import redirect_to
from website.models import Premio, Categoria, GrupoDeTarefas, Conta, MovimentacaoDeConta

def renderiza_pagina(request, pagina, id_adsense, id_adsense_horizontal, extra=None):
    contexto = {
        'nome': pagina,
        'classe_corpo': 'corpo-%s' % pagina,
        'id_adsense': id_adsense,
        'id_adsense_horizontal': id_adsense_horizontal,
        'usuario': request.user,
    }
    if extra:
        contexto.update(extra)

    return render_to_response(
        '%s.html' % pagina,
        contexto,
        context_instance=RequestContext(request))

def home(request):
    return renderiza_pagina(request, 'home', '4123834212', '9752618414')

def home_a(request):
    return redirect_to(request, '/')

def premios(request, slug=None):
    categorias = Categoria.objects.all()
    lista_premios = Premio.objects.all()
    busca = request.GET.get('q', '')
    categoria = request.GET.get('cat', '')
    queryString = ''
    if busca or categoria:
        queryString = "?q=%s&cat=%s" % (busca, categoria)
        if categoria:
            categoria = int(categoria)
            lista_premios = lista_premios.filter(categoria=categoria)
        if busca:
            lista_premios = lista_premios.filter(nome__icontains=busca)

    premio = None
    if slug:
        premio = Premio.objects.get(slug=slug)

    return renderiza_pagina(
        request,
        'premios',
        '4123834212',
        '9752618414',
        {
            'premio': premio,
            'lista_premios': lista_premios,
            'categorias': categorias,
            'cat': categoria,
            'busca': busca,
            'queryString': queryString
        }
    )

def tarefas(request):
    grupo_de_tarefas = GrupoDeTarefas.objects.all()
    return renderiza_pagina(request, 'tarefas', '4123834212', '9752618414', { 'grupo_de_tarefas': grupo_de_tarefas })


def _pagina_para_executor(request, conta):
    movimentacoes = MovimentacaoDeConta.objects.filter(conta=conta).order_by('data')
    return renderiza_pagina(request, 'saldo', '4123834212', '9752618414', { 'movimentacoes': movimentacoes, 'conta': conta })

def _pagina_para_responsavel(request):
    return renderiza_pagina(request, 'saldo', '4123834212', '9752618414')

@login_required
def saldo(request):
    conta = Conta.objects.filter(usuario=request.user)
    if conta.exists():
        return _pagina_para_executor(request, conta[0])

    return _pagina_para_responsavel(request)


@login_required
def pedidos(request):
    return renderiza_pagina(request, 'pedidos', '4123834212', '9752618414')

def regulamento(request):
    return renderiza_pagina(request, 'regulamento', '4123834212', '9752618414')