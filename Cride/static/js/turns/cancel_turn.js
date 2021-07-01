$(document).ready(function(){

        $('#btn-ver').click(function(){

        user_email = $('#user_email').val();
        $('#btn-cancel-m1').click();
        getReservedTurns(user_email);

        });



        $('#btn-delet').click(function(){
            let id_turn = $('input[name=item-turn]:checked').attr("id");
             if(id_turn){
                 swal({
                    title: "¿Estas seguro?",
                    text: "Se eliminara el turno reservado",
                    type: "warning",
                    showCancelButton: true,
                    confirmButtonColor: "#DD6B55",
                    confirmButtonText: "Si, eliminalo!",
                    cancelButtonText: "Cancelar!",
                    closeOnConfirm: false,
                    closeOnCancel: false,
                }, function (isConfirm) {
                    if(isConfirm){
                        deletTurns(id_turn);
                    }else{
                        swal("Cancelado", "Su servicio no se ha borrado :)", "error");
                    }
                });
            }else{
                swal({
                    title: "Debe seleccionar un turno",
                    text: "Seleccione el turno que desea eliminar"
                });
            }
        });





        function getReservedTurns(user_email){

            var url = "/turns/ajax/get_reserved_turns/"
            var request = $.ajax({
                type: "GET",
                url: url,
                data: {
                    "user_email": user_email
                },
            });
            request.done(function(response){

                let turns = response.turns;
                $('.tablaturnos').empty();
                for (var i = 0; i <turns.length; i++) {
                    let infoturn = turns[i].split(",");
                    let fila = "<tr class='read'>";
                    fila += '<td class="check-mail"><input id="'+infoturn[3]+'" type="radio" class="i-checks" name="item-turn"></td>';
                    fila += '<td class="mail-ontact">'+infoturn[4]+'</td>';
                    fila += '<td class="mail-ontact">'+infoturn[1]+'</td>';
                    fila += '<td class="mail-ontact">'+infoturn[2]+'</td>';
                    fila += '<td class="mail-ontact">'+infoturn[0]+'</td>';
                    fila += '</tr>';
                    $('.tablaturnos').append(fila);
                }

            });
        }

       function deletTurns(id_turn){

            var url = "/turns/ajax/delet_turns/"
            var request = $.ajax({
                type: "GET",
                url: url,
                data: {
                    "id_turn": id_turn
                },
            });
            request.done(function(response){
                if(response.valid){
                    swal("Borrado!", "Se ha eliminado tu turno.", "success");
                }else{
                    swal("Error", "No hemos podido eliminar su turno", "error");

                }
            });
        }
});