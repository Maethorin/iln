$(function() {
    $('.lista-premios').menuLista({itens: premios, usaStorage: false});
    $('#botao-limpar').bind('click', function() {
        this.form.method = 'POST';
        this.form.submit();
    });

    $('td.cor').bind('click mouseover', function() {
        var $cor =$(this).find('.premio-cor').eq(0);
        var $nome =$(this).find('.premio-nome').eq(0);
        if ($cor.hasClass('ativo')) {
            $cor.removeClass('ativo');
            $nome.removeClass('ativo');
        }
        else {
            $cor.addClass('ativo');
            $nome.addClass('ativo');
        }
    });

    $('td.cor').bind('mouseout', function() {
        $(this).find('.premio-cor').removeClass('ativo');
        $(this).find('.premio-nome').removeClass('ativo');
    });
});
