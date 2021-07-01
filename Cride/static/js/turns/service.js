$(document).ready(function(){

    $("#btn-service-next").click(function(){
        if(validInputs()){
            $(".service").addClass("sr-only");
            $(".listdays").removeClass("sr-only");
        }
    });

    $("#btn-service-back").click(function(){
        $(".service").addClass("sr-only");
        $(".entity").removeClass("sr-only");
    });

    function validInputs(){
        valid = true;

        if($("#id_name_service").val()==="" || $("#id_name_service").val().length >=254){
            $(".name-service").addClass("has-error");
            valid =  false;
        }else{
            $(".name-service").removeClass("has-error");
        }

        if($("#id_duration").val()===""){
            $(".duration").addClass("has-error");
            valid =  false;
        }else{
            $(".duration").removeClass("has-error");
        }

        if($("#max_days").val()===""){
            $(".max_days").addClass("has-error");
            valid =  false;
        }else{
            $(".max_days").removeClass("has-error");
        }

        if($("#id_max_turn_simultaneous").val()===""){
            $(".max_turn_simultaneous").addClass("has-error");
            valid =  false;
        }else{
            $(".max_turn_simultaneous").removeClass("has-error");
        }

        return valid;
    }

     $('#id_duration').keypress(function(key) {
            if((key.charCode < 48 || key.charCode > 57) && (key.charCode != 0)){
                return false;
            }
            return true;
    });

    $('#id_max_days').keypress(function(key) {
            if((key.charCode < 48 || key.charCode > 57) && (key.charCode != 0)){
                return false;
            }
            return true;
    });

    $('#id_max_turn_simultaneous').keypress(function(key) {
            if((key.charCode < 48 || key.charCode > 57) && (key.charCode != 0)){
                return false;
            }
            return true;
    });
});