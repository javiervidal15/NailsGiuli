$(document).ready(function(){

    let id_service = "";
         $('#servicio li').click(function(){
    
            id_service = $(this).attr('id');
            $('#id_turn_service').val(id_service);
            getDates(id_service);
    
    
            });
    
            $('#id_turn_date').change(function(){
            selected_date = $('#id_turn_date').val();
            getTurns(id_service,selected_date);
    
            });
    
        function createTurns(hora1, hora2, dic, duracion){
        //Obtengo hora y minuto de inicio y hora y minuto de fin
            let hour_aux_start = hora1.split(":"),
            hour_aux_end = hora2.split(":"),
            //Creo dos nuevas horas
            t1 = new Date(),
            t2 = new Date();
    
            today = new Date();
            //Le instacio la hora y minuto de inicio y fin
            t1.setHours(parseInt(hour_aux_start[0]));
            t1.setMinutes(parseInt(hour_aux_start[1]));
            t2.setHours(parseInt(hour_aux_end[0]));
            t2.setMinutes(parseInt(hour_aux_end[1]));
            //Mientras que t1 (Hora de inicio que se le suma la duracion) sea distinta de la hora final
            while((t1.getHours()!=t2.getHours()) || (t1.getMinutes()!= t2.getMinutes())){
                //Creo un posible turno
                let turno = ("0"+String(t1.getHours())).slice(-2) +":"+ ("0"+String(t1.getMinutes())).slice(-2);
                //Pregunto si ese turno ya existe en el diccionario de turnos asignados
                if(dic.indexOf(turno) == (-1)){
                    //Agrego el turno al select
                    //Pregunto si es mayor a ahora
                    if(t1>today){
                        $('#id_turn_hour').append(new Option(turno, turno, false, false));
                    }
                }
                //Sumo la duracion a t1
                t1.setMinutes(t1.getMinutes()+parseInt(duracion));
            };
        }
    
        function getDates(){
            var url = "/turns/ajax/get_dates/"
                var request = $.ajax({
                    type: "GET",
                    url: url,
                    data: {
                        "id_service": id_service,
                    },
                });
                request.done(function(response){
    
                    let dates = JSON.parse(response.unavailables_days)
    
                    let dicDatesUnavailables = new Array();
                    for (let i = 0; i < dates.length; i++) {
                        date = dates[i].fields.date.split('-');
                        date = date[2] + '/' + date[1] + '/' + date[0];
                        dicDatesUnavailables.push(date);
                    }
    
                    let not_work = response.not_work.split(",");
                    let dicNotWork = new Array();
                    for(let i = 0 ; i<not_work.length-1; i++){
                        if(parseInt(not_work[i])===7){
                            dicNotWork.push(0);
                        }else{
                            dicNotWork.push(parseInt(not_work[i]));
                        }
                    }
                    console.log(dicNotWork);
    
                    let fechaDeHoy = response.today;
                    fechaDeHoy = fechaDeHoy.split('/');
                    let day = parseInt(fechaDeHoy[0]);
                    //Aca al mes se le resta 1 por que javascript cuenta los meses de 0 a 11.
                    let month = parseInt(fechaDeHoy[1])-1;
                    let year = parseInt(fechaDeHoy[2]);
    
                    let today = new Date();
                    today.setFullYear(year,month,day);
    
                    let days_list = ["Domingo","Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"];
                    $('#id_turn_date').html('');
    
                    for (var i = 0; i < parseInt(response.max_days); i++) {
    
                    let date = ("0" + String(today.getDate())).slice(-2)+'/'+("0" + String(today.getMonth()+1)).slice(-2)+'/'+String(today.getFullYear());
                    let date_show = days_list[today.getDay()] + " " + ("0" + String(today.getDate())).slice(-2)+'/'+("0" + String(today.getMonth()+1)).slice(-2);
                    if(dicDatesUnavailables.indexOf(date) == (-1) && dicNotWork.indexOf(today.getDay()) == (-1)){
                        //Agrego la fecha al select
                        $('#id_turn_date').append(new Option(date_show, date, false, false));
                    }
    
                    today.setHours(today.getHours() +24);
                    };
                    selected_date = $('#id_turn_date').val();
    
                    getTurns(id_service,selected_date);
    
                });
        }
        //Funcion que obtiene los turnos disponibles para el servicio correspondiente al id recibido por parametro
        function getTurns(id_service,selected_date) {
    
            var url = "/turns/ajax/get_service_turns/"
                var request = $.ajax({
                    type: "GET",
                    url: url,
                    data: {
                        "id_service": id_service,
                        "selected_date": selected_date,
                    },
                });
                request.done(function(response) {
                    let duracion = response.duration;
                    let turnos = response.turnos.split(",");
                    let horas = JSON.parse(response.horas);
                    $('#id_turn_hour').empty();
    
    
    
    
                    let dic = new Array();
                    for (let i = 0; i < turnos.length-1; i++) {
                        dic.push(turnos[i]);
                    }
    
                    let hora1 = horas[0].fields.start;
                    let hora2 = horas[0].fields.end;
    
                    createTurns(hora1,hora2,dic,duracion);
    
                    let hora3 = "";
                    let hora4 = "";
                    //Si trabaja en dos horarios diferentes vuelve a hacer lo mismo con esas horas
    
                    if(horas.length==2){
    
                        hora3 = horas[1].fields.start;
                        hora4 = horas[1].fields.end;
                        createTurns(hora3,hora4,dic,duracion);
    
                    }
    
    
    
    
        });
    
    
    
    }});