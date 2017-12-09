from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.conf import settings
from pugio import views
from pugio.views import home, masters
from pugio.views import ListaProvincia, ListaImpuesto, ListaPoblacion, ListaMoneda, ListaEmpresa
from pugio.views import ListaSucursal
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^masters/', views.masters, name='masters'),
    url(r'^provincia/',ListaProvincia.as_view(), name = 'ListaProvincia'),
    url(r'^impuesto/',ListaImpuesto.as_view(), name = 'ListaImpuesto'),
    url(r'^poblacion/',ListaPoblacion.as_view(), name = 'ListaPoblacion'),
    url(r'^moneda/',ListaMoneda.as_view(), name = 'ListaMoneda'),
    url(r'^empresa/',ListaEmpresa.as_view(), name = 'ListaEmpresa'),
    url(r'^sucursal/',ListaSucursal.as_view(), name = 'ListaSucrusal'),
]

if settings.DEBUG:
     urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
