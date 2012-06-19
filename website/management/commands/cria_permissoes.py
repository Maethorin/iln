#!/usr/bin/env python
# encoding: utf-8

from django.core.management.base import BaseCommand
from website.management.commands import cria_permissao

PERMISSOES = [
    ('pode_ver_saldo', 'Pode ver saldo.', 'Conta'),
    ('pode_incluir_pontos', 'Pode incluir pontos', 'Conta'),
    ('pode_resgatar', 'Pode resgatar', 'Premio'),
    ('pode_marcar_tarefa_como_concluida', 'Pode marcar tarefa como concluida', 'Tarefa'),
    ('pode_finalizar_tarefa', 'Pode finalizar tarefa', 'Tarefa'),
]

class Command(BaseCommand):
    help = "Cria todas as permissões customizadas do website. Precisa do comando cria_permissao"

    def handle(self, *args, **options):
        command = cria_permissao.Command()
        for permissao in PERMISSOES:
            command.handle(codigo=permissao[0], nome=permissao[1], model=permissao[2])
