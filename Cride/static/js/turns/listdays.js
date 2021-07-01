$(document).ready(function(){

    let contador = 0;


    //Funciones que se ejecutan al comenzar
    $('.clockpicker').clockpicker();


    $("#btn-listdays-back").click(function(){
        $(".service").removeClass("sr-only");
        $(".listdays").addClass("sr-only");
    });


});
