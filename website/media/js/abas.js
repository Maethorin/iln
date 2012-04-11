
$(function() {
    $(".abas li").each(function() {
        var $this = $(this);
        var $a = $this.find('a')
        var texto = $a.text();
        $a.remove();
        $this.text(texto);
    });
    $(".abas li").bind("click", function() {
        if ($(this).hasClass("ativa")) {
            return false;
        }
        window.location = "/" + $(this).attr("class");
    });
});
