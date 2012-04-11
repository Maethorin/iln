function distribuiTarefas($tarefas) {
    var $grupo = $tarefas.parent();
    var $div = $('<div class="container-de-tarefas"></div>').appendTo($grupo);
    var $tarefas2 = $('<ul class="tarefas"></ul>').appendTo($div);
    $tarefas.find('li.tarefa').each(function(index, item) {
        if (index % 2 != 0) {
            $(item).appendTo($tarefas2);
        }
    });
    $tarefas.prependTo($div);
}

function redistribuiTarefas($grupo) {
    var $div = $grupo.find('.container-de-tarefas');
    var $tarefas = $div.find('ul.tarefas').eq(0);
    var $listaTarefas = $tarefas.find('li.tarefa');
    var $tarefas2 = $div.find('ul.tarefas').eq(1);
    var $listaTarefas2 = $tarefas2.find('li.tarefa');
    $listaTarefas.each(function(index, item) {
        if (index <= $listaTarefas2.length) {
            $listaTarefas2.eq(index).remove().insertAfter($(item));
        }
    });
    $tarefas.appendTo($grupo);
    $tarefas2.remove();
    $div.remove();
}

function expandeGrupo($grupo) {
    $('.nome-tarefa').unbind().bind('click', clickNoNomeDaTarefa);
    var posicaoAtual = $grupo.offset();
    $grupo.data('posicaoAtual', posicaoAtual);
    $grupo.data('widthAtual', $grupo.width());

    $grupo.css('top', posicaoAtual.top);
    $grupo.css('left', posicaoAtual.left);
    $grupo.css('margin', '0');

    $grupo.css('position', 'absolute');
    insereGrupoVazioNoLugarDo($grupo);
    distribuiTarefas($grupo.find('ul.tarefas'));
    $grupo.animate({
        width: '750px',
        left: '257',
        top: '260'
        },
        'fast',
        function() {
            $grupo.addClass('ativo');
            $grupo.find('.container-de-tarefas').animate({ height: 'show' }, 'fast');
            $grupo.find('ul.tarefas').show('fast');
            $grupo.find('.fechar-grupo').show('fast');
        }
    );
    $grupo.find('.nome-grupo').unbind();
}

function colapsaGrupo($grupo) {
    $grupo.find('li.tarefa').each(function() {
        fechaTarefa($(this));
    });
    $grupo.find('ul.tarefas').hide('fast');
    $grupo.find('.fechar-grupo').hide('fast');
    $grupo.find('.container-de-tarefas').animate(
        { height: 'hide' },
        'fast',
        function() {
            $grupo.removeClass('ativo');
            $grupo.animate({
                    width: $grupo.data('widthAtual'),
                    left: $grupo.data('posicaoAtual').left,
                    top: $grupo.data('posicaoAtual').top
                },
                'fast',
                function () {
                    $('.vazio').remove();
                    $grupo.removeAttr('style');
                    $grupo.find('.nome-grupo').bind('click', clickNoNomeDoGrupo);
                    redistribuiTarefas($grupo);
                }
            );
        }
    );
}

var insereGrupoVazioNoLugarDo = function($grupo) {
    var $vazio = $([
        '<li class="grupo vazio">',
            '<h3 class="nome-grupo">',
                $grupo.find('.nome-grupo').text().replace(' X', ''),
            '</h3>',
        '</li>'
    ].join(''));
    $vazio.insertBefore($grupo);
};

var clickNoNomeDoGrupo = function() {
    var $this = $(this);
    if (!$this.hasClass('ativo')) {
        expandeGrupo($this.parent());
    }
};

var clickNoFecharGrupo = function(event) {
    var $grupo = $(this).parents('.grupo');
    colapsaGrupo($grupo);
    event.stopPropagation();
};

function fechaTarefa($tarefa) {
    $tarefa.find('.dados-da-tarefa').animate({height: 'hide'}, 'fast', function() {
        $tarefa.removeClass('ativo');
        $tarefa.find('.controle-do-colapsar').text('>');
    });
}

var clickNoNomeDaTarefa = function() {
    var $this = $(this);
    if ($this.parent().hasClass('ativo')) {
        fechaTarefa($this.parent());
    }
    else {
        $this.parent().find('.dados-da-tarefa').animate({height: 'show'}, 'fast', function() {
            $this.parent().addClass('ativo');
            $this.find('.controle-do-colapsar').text('v');
        });
    }
};

$(function() {
    $('.nome-tarefa').append('<span class="controle-do-colapsar">></span>');
    $('.nome-grupo').bind('click', clickNoNomeDoGrupo).append('<span class="fechar-grupo">X</span>');
    $('.fechar-grupo').bind('click', clickNoFecharGrupo);
});