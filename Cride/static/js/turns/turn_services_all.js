 $(document).ready(function() {
    $('.footable').footable();
    $('.footable-sort-indicator').remove();

    $("#btn-trash").click(function(){
        let pk_service = $('input[name=pk-service]:checked').attr("id");
        if(pk_service){
            swal({
                title: "¿Estas seguro?",
                text: "No podrá recuperar este servicio!",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Si, borralo!",
                cancelButtonText: "Cancelar!",
                closeOnConfirm: false,
                closeOnCancel: false,
            }, function (isConfirm) {
                if(isConfirm){
                    deleteService();
                }else{
                    swal("Cancelado", "Su servicio no se ha borrado :)", "error");
                }
            });
        }else{
            swal({
                title: "Debe seleccionar un servicio",
                text: "Seleccione el servicio que va a eliminar, para no recibir mas turnos."
            });
        }
    });

    function deleteService(){
        var url = '/turns/ajax/delete_service/';
        var pk_service = $('input[name=pk-service]:checked').attr("id");
        if(pk_service){
            let request = $.ajax({
                type: "GET",
                url: url,
                data: {
                    "pk_service":pk_service,
                },
            });
            request.done(function(response){
                if(response.success==="true"){
                    let i = $('#'+pk_service).parent().parent().remove();
                    swal("Borrado!", "Se ha eliminado tu servicio.", "success");
                }else{
                    swal("Error", "No pudimos eliminar su servicio", "error");
                }
            });
        }
    };

    $("#btn-edit").click(function(){
        let pk_service = $('input[name=pk-service]:checked').attr("id");
        if(pk_service){
            window.location.href = "/turns/services/edit/"+ pk_service + "/";
        }else{
            swal({
                title: "Debe seleccionar un servicio",
                text: "Seleccione el servicio que va a editar"
            });    
            
        }
    });
});