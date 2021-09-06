"""Main URLs module."""
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from turns import views as turns_views
from home import views as home_views
from django.conf.urls import url,include

import turns

urlpatterns = [
    # Django Admin
    #url(r'nueva/orden/de/trabajo/$', login_required(NuevaOrdenTrabajo), name='nueva_orden_trabajo'),
    url(r'^login/$',home_views.login_view,name="login"),
    url(r'^turnos/reservar/$',turns_views.turn_new,name="reservar_turno"),
    url(r'^dashboard/home$',home_views.dashboard_home,name="dashboard_home")]
