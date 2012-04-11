$(function() {
    $('.lista-premios').menuLista({itens: premios, usaStorage: false});
    $('#botao-limpar').bind('click', function() {
        this.form.method = 'POST';
        this.form.submit();
    });
});
