"""Main URLs module."""

from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from turns import views as turns_views
from django.views.generic import TemplateView
from django.conf.urls import url,include

urlpatterns = [
    # Django Admin

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    path(settings.ADMIN_URL, admin.site.urls),
    url(r'^home/', include('home.urls')),
    url(r'^turns/', include('turns.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
