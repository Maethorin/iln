#!/usr/bin/env python
# encoding: utf-8
from optparse import make_option

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Cria a permssão passada"

    option_list = BaseCommand.option_list + (
        make_option("-a", "--app", dest="app", default='website'),
        make_option("-m", "--model", dest="model", default=None),
        make_option("-c", "--codigo", dest="codigo", default=None),
        make_option("-n", "--nome", dest="nome", default=None),
    )

    def handle(self, *args, **options):
        app = options.get("app", 'website')
        model = options.get("model", None)
        codigo = options.get("codigo", None)
        nome = options.get("nome", None)
        if not model or not codigo or not nome:
            print "Parâmetros incorretos. Comando mínimo deve ter model, codigo e nome. Ex.: cria_permisao -c pode_criar -n 'Pode criar' -m Usuario"
            exit(1)

        content_type = ContentType.objects.get(app_label=app, model=model)
        if Permission.objects.filter(codename=codigo,
                                       name=nome,
                                       content_type=content_type).exists():
            mensagem = u'Permissão "%s" não foi criada para o model %s.%s, pois já existe.' % (nome, app, model)
            linha = '-' * len(mensagem)
            print("\033[31m%s" % linha)
            print(mensagem)
            print("%s\033[0m" % linha)
        else:
            Permission.objects.create(codename=codigo,
                                       name=nome,
                                       content_type=content_type)
            mensagem = u'Permissão "%s" criada com sucesso para o model %s.%s' % (nome, app, model)
            linha = '-' * len(mensagem)
            print("\033[32m%s" % linha)
            print(mensagem)
            print("%s\033[0m" % linha)
