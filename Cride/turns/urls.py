from django.conf.urls import url
from turns.ajax import *
from turns.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    # url(r'^search/$', TurnSearch, name='turn_search'),
     url(r'^end/(?P<id_client>\d{1,1000000})/(?P<id_turn>\d{1,1000000})/$', TurnEnd, name='turn_end'),
    # url(r'^new/$', TurnAllNew, name='turn_new'),
    # url(r'^my/page/$', login_required(MyPage), name='turn_my_page'),
    # url(r'^services/edit/(?P<pk_service>\d*)/$', login_required(ServiceEdit), name='turn_services_edit'),
    # url(r'^services/new/$', login_required(ServiceNew), name='turn_services_new'),
    # url(r'^services/$', login_required(ServicesAll), name='turn_services_all'),
    url(r'^calendar/$', login_required(TurnsAll), name='turn_all'),
    url(r'^calendar/today/$', login_required(TurnsToday), name='turn_now'),
    url(r'^calendar/tomorrow/$', login_required(TurnsTomorrow), name='turn_tomorrow'),
    # url(r'^configurations/edit/$', login_required(EntityEdit), name='turn_entity_edit'),
    # url(r'^finish/(?P<pk_entity>\d{1,1000000})/$', TurnFinish, name='turn_finish'),
    # url(r'^home/$', TurnHome, name='turn_home'),
    # url(r'^ajax/get_valid_name_entity/$', get_valid_name_entity, name='get_valid_name_entity'),
    # url(r'^ajax/delete_service/$', login_required(get_delete_service), name='get_delete_service'),
    url(r'^ajax/get_turns/$', login_required(get_turns), name='get_turns'),
    url(r'^ajax/get_calendar/$', login_required(get_calendar), name='get_calendar'),
    url(r'^ajax/cancel_day/$', login_required(cancel_day), name='cancel_day'),
    url(r'^ajax/get_dates/$', get_dates, name='get_dates'),
    url(r'^ajax/get_reserved_turns/$', get_reserved_turns, name='get_reserved_turns'),
    url(r'^ajax/delet_turns/$', delet_turn, name='delet_turns'),
     url(r'^ajax/get_service_turns/$', get_turns_service, name='get_service_turns')
    # url(r'^now/$', now, name='now'),
    # url(r'^now/$', now_end, name='now_end'),

]

