$(document).ready(function(){
    let extension_url = false;

    //Si el input extension url tiene algun valor lo valida al cargar la pagina
    if($("#id_extension_url").val().length != 0){
        getValid();
    };

    //Funcion que pregunta mediante ajax si es valido el nombre de la extension url
    $("#id_extension_url").keyup(function(){getValid();});
    function getValid() {
        var url = "/turns/ajax/get_valid_name_entity/";
        var name_entity = $("#id_extension_url").val();
        if (name_entity) {
            // Eliminamos el texto anterior
            $("#error-name-entity").html("");
            var request = $.ajax({
                type: "GET",
                url: url,
                data: {
                    "name_entity": name_entity,
                },
            });
            request.done(function(response) {
                if(response.valid==="true"){
                    $("#link").removeClass("has-error");
                    $("#btn-entity").attr("disabled",false);
                    extension_url=true;
                }else{
                    $("#link").addClass("has-error");
                    $("#btn-entity").attr("disabled",true);
                    extension_url=false;
                }
                $("#id_extension_url").trigger("change");
            });
        } else {
            $("#link").addClass("has-error");
            $("#btn-entity").attr("disabled",true);
            $("#id_extension_url").trigger("change");
            extension_url=false
        }
    };

    //Valida los caracteres
    $('#id_name_entity').keypress(function(key) {
        return (validKey(key) || (key.charCode ==32));
    });

    //Valida los caracteres
    $('#id_name').keypress(function(key) {
        return (validKey(key) || (key.charCode ==32));
    });

    //Valida los caracteres
    $('#id_extension_url').keypress(function(key) {
        return validKey(key);
    });


    function validKey(key){
        if((key.charCode < 97 || key.charCode > 122) && (key.charCode < 65 || key.charCode > 90) && (key.charCode != 45)
             && (key.charCode < 48 || key.charCode > 57) && (key.charCode != 46) && (key.charCode != 241) && (key.charCode != 246)
              && (key.charCode != 0) && (key.charCode != 43)){
            return false;
        }
        return true;
    };

    //Click en el button siguiente
    $("#btn-entity").click(function(){
        if(validInputs()){
            $(".service").removeClass("sr-only");
            $(".entity").addClass("sr-only");
        }
    });

    //Valida que los inputs no esten vacios antes de continuar
    function validInputs(){
        let valid = true;
        if($("#id_name_entity").val()!=undefined){
            //Valida el nombre de la entidad no este vacio ni supere los caracteres maximos
            if($("#id_name_entity").val()==="" || $("#id_name_entity").val().length >=254){
                $(".name-entity").addClass("has-error");
                valid =  false;
            }else{
                $(".name-entity").removeClass("has-error");
            }
        }else{
            //Valida el nombre de la entidad no este vacio ni supere los caracteres maximos
            if($("#id_name").val()==="" || $("#id_name").val().length >=254){
                $(".name-entity").addClass("has-error");
                valid =  false;
            }else{
                $(".name-entity").removeClass("has-error");
            }
        }

        //Valida la extension url que no este vacio ni supere los caracteres maximos
        if($("#id_extension_url").val()==="" || $("#id_extension_url").val().length >=254){
            $("#link").addClass("has-error");
            valid = false;
        }else{
            if(extension_url){
                $("#link").removeClass("has-error");
            }
        }

        if($("#id_type_entity").val().trim() === ''){
            $(".type-entity").addClass("has-error");
            valid = false;
        }else{
            $(".type-entity").removeClass("has-error");
        }

        return valid;
    }

    //Completa el input extension url con lo llenado en el nombre sin espacios
   $("#id_extension_url").focusin(function() {
        let name = $("#id_name_entity").val();
        name = name.replace(/ /gi ,"");

        name = name.toLowerCase();
        $("#id_extension_url").val(name);

    });

});