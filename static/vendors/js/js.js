$(document).ready(function () {
    //**************************************************************************--- o menu lateral

    //**************************************************************************************************
    //cuando haga click sobre el btn, activar caracteristicas del CSS
    $("#menu-close").click(function (e) {
        $("#menuLateral-contenedor").toggleClass("active");
        e.preventDefault();
    });

    // abrir el menu cuando el cursor esté sobre la imagen
    $("#menu-toggle").hover(function (e) {
        $("#menuLateral-contenedor").toggleClass("active", true);
        e.preventDefault();
    });
    //abrir cuando le den click sobre la imgen del menu
    $("#menu-toggle").bind('click', function (e) {
        $("#menuLateral-contenedor").toggleClass("active", true);
        e.preventDefault();
    });
    //si el cursor está por fuera del menu, este se quita
    $('#menuLateral-contenedor').mouseleave(function (e) {
        /*! .toggleClass( className, state ) */
        $('#menuLateral-contenedor').toggleClass('active', false);
        e.stopPropagation(); //detiene eventos
        e.preventDefault(); //quita acciones predeterminadas
    });


    //****************************************************************** botones activar, inactivar, todos de las tablas
    //**************************************************************************************************
    $(".btn-group .btn").click(function () {
        var inputValue = $(this).find("input").val(); //indica si el valor del boton es activo, inact o todos
        if (inputValue != 'all') {
            var target = $('table tr[data-status="' + inputValue + '"]');
            $("table tbody tr").not(target).hide(); //oculta los que no son iguales al valor seleccionado
            target.fadeIn(); //muestra los elementos iguales al valor seleccionado
        } else {
            $("table tbody tr").fadeIn(); //muestra todas las filas
        }
    });
    //****************************************************************** validar formulario crear director
    //**************************************************************************************************
    $('#container-principal').on('submit', '#frm-crear-dir', function (event) {
        var error = 0;
        $('.requerido').each(function (i, elem) {
            if ($(elem).val() == '') {
                $(elem).css({
                    'border': '1px solid red'
                });
                error++;
            }
        });
        if (error > 0) {
            event.preventDefault();
            $('.msj-error').addClass("active");
        } else if (error === 0) {
            var msj = $('.msj-error.active'); //pone todos las diapositivas que esten activas
            msj.removeClass('active'); //desactiva la diap
        }
    });




});
