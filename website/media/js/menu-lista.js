$.widget('ui.menuLista', {
    options: {
        'usaStorage': false,
        'quantidadeMaximaDeItens': 4,
        'direcao': 'direita',
        'primeiroIndice': 0,
        'ultimoIndice': 3,
        'itens': [],
        '$setaDireita': $('<span class="seta-direita"> >> </span>'),
        '$setaEsquerda': $('<span class="seta-esquerda"> << </span>'),
        'htmlParaTemplate': [
            '<div class="threecol${last}">',
                '<a href="${slug}">',
                    '<div class="item-da-lista${selecionado}">',
                        '<div class="foto-container">',
                            '<img src="${thumbnail}" alt="Foto de ${nome}">',
                        '</div>',
                        '${nome}',
                    '</div>',
                '</a>',
            '</div>'
        ].join('')
    },
    _create: function() {
        this.element.empty();
        if (this.options.usaStorage) {
            if (sessionStorage.getItem("primeiroIndice")) {
                this.options.primeiroIndice = parseInt(sessionStorage.getItem("primeiroIndice"));
            }

            if (sessionStorage.getItem("ultimoIndice")) {
                this.options.ultimoIndice = parseInt(sessionStorage.getItem("ultimoIndice"));
            }
        }

        var contador = 0;
        if (!$.template['template']) {
            $.template('template', this.options.htmlParaTemplate);
        }

        var quantidadeDeItens = this.options.itens.length > this.options.quantidadeMaximaDeItens ? this.options.quantidadeMaximaDeItens : this.options.itens.length;
        this.options.ultimoIndice = quantidadeDeItens - 1;

        for (var indice = this.options.primeiroIndice; indice < this.options.primeiroIndice + quantidadeDeItens; indice++) {
            var indiceReal = indice;
            if (indiceReal < 0) {
                indiceReal = this.options.itens.length - indice;
            }
            if (indiceReal >= this.options.itens.length) {
                indiceReal = indice - this.options.itens.length;
            }

            if (contador == 3) {
                this.options.itens[indiceReal]["last"] = " last";
            }
            contador++;
            $.tmpl("template", this.options.itens[indiceReal]).appendTo(this.element);
        }

        if (this.options.itens.length > this.options.quantidadeMaximaDeItens) {
            this.preparaSetasDePaginacao();
        }
    },
    preparaSetasDePaginacao: function() {
        this.options.$setaDireita.insertAfter(this.element);
        this.options.$setaEsquerda.insertAfter(this.element);

        this.bindDoClickParaDireita();
        this.bindDoClickParaEsquerda();

//        this.defineVisibilidadeDeBotoesDePaginacao();
    },
//    defineVisibilidadeDeBotoesDePaginacao: function() {
//        this.options.$setaEsquerda.hide();
//        this.options.$setaDireita.hide();
//        if (this.options.itens.length > this.options.quantidadeMaximaDeItens) {
//            this.options.$setaEsquerda.show();
//            this.options.$setaDireita.show();
//        }
//    },
    atualizaIndices: function() {
        if (this.options.direcao == "direita") {
            this.options.primeiroIndice--;
            this.options.ultimoIndice--;
            if (this.options.primeiroIndice < 0) {
                this.options.primeiroIndice = this.options.itens.length - 1;
            }
            if (this.options.ultimoIndice < 0) {
                this.options.ultimoIndice = this.options.itens.length - 1;
            }
        }
        else {
            this.options.ultimoIndice++;
            this.options.primeiroIndice++;
            if (this.options.ultimoIndice == this.options.itens.length) {
                this.options.ultimoIndice = 0;
            }
            if (this.options.primeiroIndice == this.options.itens.length) {
                this.options.primeiroIndice = 0;
            }
        }
        if (this.options.usaStorage) {
            sessionStorage.setItem("primeiroIndice", this.options.primeiroIndice);
            sessionStorage.setItem("ultimoIndice", this.options.ultimoIndice);
        }
    },
    obterNovoIndice: function() {
        return this.options.direcao == "direita" ? this.options.primeiroIndice : this.options.ultimoIndice;
    },
    obterProximoItem: function() {
        this.atualizaIndices();
        var indice = this.obterNovoIndice();
        return $.tmpl("template", this.options.itens[indice]);
    },
    moveParaEsquerda: function($botao) {
        $botao.unbind();
        var $primeiro = this.element.find('.threecol:first');
        var $ultimo = this.element.find('.threecol:last');
        this.options.direcao = "esquerda";
        var $proximo = this.obterProximoItem();
        $proximo.appendTo(this.element);
        $proximo.hide();
        $proximo.width($primeiro.width());
        $proximo.addClass("last");
        $primeiro.animate({ width: "hide"}, 80, function() {
            $primeiro.remove();
            $ultimo.removeClass("last");
        });
        var _self = this;
        $proximo.animate( {width: 'show'}, 80, function() {
            $proximo.removeAttr("style");
            _self.bindDoClickParaEsquerda();
        });
    },
    moveParaDireita: function($botao) {
        $botao.unbind();
        var $ultimo = this.element.find('.threecol:last');
        var $anterior = this.element.find('.threecol').eq(2);
        this.options.direcao = "direita";
        var $proximo = this.obterProximoItem();
        $proximo.hide();
        $proximo.width($ultimo.width());
        $proximo.removeClass("last");
        $proximo.prependTo(this.element);
        $anterior.addClass("last");
        $proximo.animate({width: 'show'}, 80, function() {
            $proximo.removeAttr("style");
        });
        var _self = this;
        $ultimo.animate({width: 'hide'}, 80, function() {
            $ultimo.remove();
            _self.bindDoClickParaDireita();
        });
    },
    bindDoClickParaEsquerda: function() {
        var _self = this;
        this.options.$setaDireita.bind('click', function () {
            _self.moveParaEsquerda($(this));
        });
    },
    bindDoClickParaDireita: function() {
        var _self = this;
        this.options.$setaEsquerda.bind('click', function () {
            _self.moveParaDireita($(this));
        });
    },
    destroy: function() {
        this.element.empty();
        $.Widget.prototype.destroy.apply(this, arguments);
    }
});