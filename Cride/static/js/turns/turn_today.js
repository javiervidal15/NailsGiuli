$(document).ready(function(){

    get_turns();

    $("#services").change(function(){
        get_turns();
    });

    function get_turns(){
        var url = "/turns/ajax/get_turns/";
        var pk_service = $("#services").val();
        if(pk_service){
            var request  = $.ajax({
                type: "GET",
                url: url,
                data: {
                    "pk_service": pk_service,
                }
            });
            request.done(function(response){
                //Parseo el string a JSON
                let turns = JSON.parse(response.turns);
                //Pregunto si hay algun turno
                if(turns.length>0){
                    //Remuevo los turnos de otro servicio
                    $(".turn").remove();
                    $(".not-turn").addClass("sr-only");

                    let turn,start="",day=new Date(),aux,duration,clients="",client,end="";
                    //Recorro los turnos de hoy
                    for(var i=0; i<turns.length; i++){
                        turn = turns[i];
                        duration = turn.fields.duration;
                        start = (turn.fields.start).substr(0,5);

                        //Calculo cuando terminaria el turno
                        aux = start.split(":");
                        day.setHours(parseInt(aux[0]));
                        day.setMinutes(parseInt(aux[1]) + duration);
                        end = ("0"+String(day.getHours())).slice(-2) +":"+ ("0"+String(day.getMinutes())).slice(-2);

                       	clients="";
                        for(var j=0; j<turn.fields.clients.length; j++){
                            client= turn.fields.clients[j];
                            clients += "<p><strong>"+ client[0] + "</strong></p><p>"+ client[1] +"</p>";
                        }

                        //Agrego el turno html
                        $("#list-turn").append(
                        "<div class='timeline-item turn'>"+
                            "<div class='row'>"+
                                "<div class='col-xs-3 date'>"+
                                    "<i class='fa fa-ticket'></i>"+
                                     start+ "<br>"+ end +
                                    "<br/>"+
                                    "<small class='text-navy'>"+ turn.fields.state +"</small>"+
                                "</div>"+
                                "<div class='col-xs-7 content'>"+
                                    clients+
                                "</div>"+
                            "</div>"+
                        "</div>");
                    };
                }else{
                    $(".turn").remove();
                    $(".not-turn").removeClass("sr-only");
                }
            });
        }
    };
});
