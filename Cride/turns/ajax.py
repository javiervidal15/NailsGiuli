from django.http import JsonResponse
import datetime
from turns.models import Service, Turn, Assigned,TypeUnavailableDay, Client
from django.core import serializers


def get_turns(request):
    pk_service = request.GET.get('pk_service','')
    turns = Turn.objects.filter(service_id=pk_service,date_turn=datetime.date.today())

    response={}
    response["turns"] = serializers.serialize('json', turns, fields=('duration','start','state','clients'),
                                              use_natural_foreign_keys=True)

    return JsonResponse(response)


def get_dates(request):

    id_service = request.GET.get('id_service','')

    # Obtengo el servicio
    service = Service.objects.get(id=id_service)

    # Obtengo una lista de los dias en que no trabaja
    unavailables_days = service.get_day_not_available().all()
    today = "%i/%i/%i" % (datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year)

    not_work = ""
    for day in service.get_days_turn().all():
        if not day.is_available():
            not_work+= str(day.get_day().id)+","

    response = {}
    response["unavailables_days"] = serializers.serialize('json', unavailables_days, fields=('date'))
    response["not_work"] = not_work
    response["today"] = today
    response["max_days"] = service.get_max_days()
    return JsonResponse(response)



def get_reserved_turns(request):

    user_email = request.GET.get('user_email')

    #Verifico si existe el email
    client = Client.objects.filter(email = user_email)
    if len(client) == 0:
        response = {}
        response["existe"] = "False"
        return JsonResponse(response)
    else:
        client = client[0]
    #Obtengo los turnos para ese usuario
        turns = Turn.objects.filter(clients=client)
        response = {}
        turnos = []
        for turn in turns:
            if(turn.get_state().get_name() == "Asignado"):
                turnos.append("%s,%s,%s,%s,%s" %("Giuli Nails",turn.get_start(),turn.get_service().get_name(),str(turn.id),
                                              turn.get_date()))

        response["turns"] = turnos
        return JsonResponse(response)


    response = {}
    return JsonResponse(response)


def delet_turn(request):
    id_turn = request.GET.get('id_turn')
    Turn.objects.filter(id=id_turn).delete()

    response = {}
    response['valid'] = "true"
    return JsonResponse(response)


def get_delete_service(request):
    pk_service = request.GET.get('pk_service','')

    response={}

    if Service.objects.filter(id=pk_service).exists():
        service = Service.objects.get(id=pk_service)
        service.delete()
        response["success"] = "true"
    else:
        response["success"] = "false"

    return JsonResponse(response)


def sumar_hora(hora1, hora2):
    formato = "%H:%M"
    lista = hora2.split(":")
    hora = int(lista[0])
    minuto = int(lista[1])
    h1 = datetime.strptime(hora1, formato)
    dh = datetime.timedelta(hours=hora)
    dm = datetime.timedelta(minutes=minuto)
    resultado1 = h1 + dm
    resultado = resultado1 + dh
    resultado = resultado.strftime(formato)
    return str(resultado)


def get_turns_service(request):
    id_service = request.GET.get('id_service','')
    # El formato de la fecha actual es dd/mm/yyyy
    selected_date = request.GET.get('selected_date','')
    selected_date = selected_date.split('/')
    # Instancio la fecha
    year = int(selected_date[2])
    month = int(selected_date[1])
    day = int(selected_date[0])

    # Django maneja fechas en formato yyyy-mm-dd
    selected_date = selected_date[2] + '-' + selected_date[1] + '-' + selected_date[0]

    # Diccionario para tener el dia de la semana correspondiente a la fecha seleccionada por el user
    dicdias = {'MONDAY': 'Lunes', 'TUESDAY': 'Martes', 'WEDNESDAY': 'Miercoles', 'THURSDAY': 'Jueves',
               'FRIDAY': 'Viernes', 'SATURDAY': 'Sabado', 'SUNDAY': 'Domingo'}


    fecha = datetime.date(year, month, day)

    # Obtengo el dia
    week_day = (dicdias[fecha.strftime('%A').upper()])

    # Obtengo el servicio
    service = Service.objects.get(id=id_service)
    # Obtengo una lista de sus dias de trabajo
    days_turn = service.get_days_turn().all()

    # Recorro la lista y busco el dia de la semana correspondiente para obtener su horario
    hours = []
    for day in days_turn:
        if(day.get_day().get_name()==week_day):
            # Si el dia es igual al dia seleccionado ejemplo: Lunes==Lunes, obtengo sus horas
            hours = day.get_hours().all()

    print(hours)

    # Calculamos los turnos disponibles.

    # Obtengo todos los turnos en estado asignado
    turns = Turn.objects.filter(service=service, date_turn=selected_date, state=Assigned.objects.all().first())
    # Obtengo la duracion del turno
    assigned_turns = ""
    for turn in turns:
        if not len(turn.get_clients().all())<service.get_max_turn_simultaneous():
            assigned_turns += "%s," %turn.get_start()

    duration = service.get_duration()

    #Obtengo una lista de los dias en que no trabaja
    unavailables_days = service.get_day_not_available().all()
    today = "%i/%i/%i" %(datetime.datetime.now().day,datetime.datetime.now().month,datetime.datetime.now().year)

    response = {}
    response["unavailables_days"] = serializers.serialize('json', unavailables_days, fields=('date'))
    response["today"] = today
    response["turnos"] = assigned_turns

    response["horas"]= serializers.serialize('json', hours, fields=('start','end'))

    response["duration"] = str(duration)

    return JsonResponse(response)


def get_calendar(request):
    id_service = request.GET.get('pk_service','')
    service = Service.objects.get(id=id_service)

    if Service.objects.filter(id=service.id).exists():
        month_from =  datetime.datetime.now().month
        year_from = datetime.datetime.now().year
        month_until = month_from +1
        year_until = year_from
        if month_until>12:
            month_until = 1
            year_until += 1

        response = {}

        response["days_turn"]= serializers.serialize("json",service.get_days_turn().all(),fields=('available','day','hours'),
                                                     use_natural_foreign_keys=True)
        response["days_not_available"] = serializers.serialize("json",service.get_day_not_available().all(),fields=('date','motive'),
                                                               use_natural_foreign_keys=True)

        response["turns"] = serializers.serialize("json",Turn.objects.filter(date_turn__month__gte=month_from,
                                                                             date_turn__month__lte =month_until,
                                                                             date_turn__year__gte=year_from,
                                                                             date_turn__year__lte =year_until,
                                                                             service=service),
                                                  fields=('duration','start','state','clients','id','date_turn'),use_natural_foreign_keys=True)

    print(response)
    return JsonResponse(response)


def cancel_day(request):
    id_motive = request.GET.get("pk_motive","")
    date = request.GET.get("date","")
    id_service = request.GET.get('pk_service',"")
    date_now = datetime.datetime.now().date()
    valid = False

    if Service.objects.filter(id=id_service).exists() and date > str(date_now):
        motive = TypeUnavailableDay.objects.get(id=id_motive)
        if motive.is_all_services():
            for service in Service.objects.all():
                service.day_not_available.create(date=date, motive_id=id_motive)

            turns = Turn.objects.filter(date_turn=date)
            #for t in turns:
                #t.notify_cancel()
            turns.delete()
        else:
            service = Service.objects.get(id=id_service)
            service.day_not_available.create(date=date,motive_id=id_motive)
            turns = Turn.objects.filter(service=service,date_turn=date)
            for t in turns:
                t.notify_cancel()
            turns.delete()
        valid = True

    response={}
    response["valid"] = valid

    return JsonResponse(response)
