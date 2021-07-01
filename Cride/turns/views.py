from django.shortcuts import render
from django.http import HttpResponse
from turns.models import *
from turns.forms import *
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse




# Create your views here.

def list_turns(request):

    turns = [1,2,3]
    return HttpResponse(str(turns))
#    return render(request,"template.html",{"name":"javier"})



def turn_new(request):

    services = Service.objects.all()
    not_turn = False

    if request.method == "POST":
        form = RegisterTurnFormWithDoc(request.POST)
        if form.is_valid():

            turn_date = form.cleaned_data["turn_date"].split('/')
            turn_hour = form.cleaned_data["turn_hour"]
            turn_date = turn_date[2] + '-' + turn_date[1] + '-' + turn_date[0]
            turns = Turn.objects.filter(start=turn_hour,date_turn=turn_date)
            id_service = form.cleaned_data["turn_service"]
            service = Service.objects.get(id=id_service)

            turns_simultaneous = service.get_max_turn_simultaneous()
            duration = service.get_duration()

            if(len(turns)==0):
                turn = Turn(duration=duration,date_turn=turn_date,start=turn_hour,
                            service=service,state=Assigned.objects.all().first())
                turn.save()
            else:
                turn = turns.first()

            if len(turn.get_clients().all())<turns_simultaneous:
                email = form.cleaned_data["email"]
                if Client.objects.filter(email=email).exists():
                    client = Client.objects.get(email=email)
                    if not Turn.objects.filter(id=turn.id,clients__in=[client.id]).exists():
                        turn.clients.add(client)

                else:
                    client = Client(email=email,full_name=form.cleaned_data["name"])
                    client.save()
                    turn.clients.add(client)
                    # ACA TAMBIEN HABRIA QUE ENVIAR LA HORA DE INICIO DEL TURNO DESPUES DE OBTENERLA POR EL FORM

                return HttpResponseRedirect(reverse('turn_end',kwargs={"id_client":client.id,"id_turn":turn.id}))

            else:
                not_turn = "No hay turnos disponibles a esta hora, intente nuevamente"
                form.add_error("turn_hour",not_turn)
    else:
        form = RegisterTurnFormWithDoc()
    today = "%i/%i/%i" %(datetime.datetime.now().day,datetime.datetime.now().month,datetime.datetime.now().year)

    return render(request,'new_turn.html',{"form":form,"services":services,"today":today,"not_turn":not_turn })
