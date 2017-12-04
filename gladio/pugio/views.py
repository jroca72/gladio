from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime, timedelta
from django.utils import timezone
from django.views.generic import ListView, DetailView
from pugio.models import provincia,impuesto 

# vistas -----------------------------------------------------
def home(request):
	return render(request, 'pugio/home.html')

def masters(request):
	return render(request, 'pugio/masters.html')

class ListaProvincia(ListView):
    queryset = provincia.objects.order_by('numero')
    context_object_name = 'provincia'
    paginate_by = 10

class ListaImpuesto(ListView):
	queryset = impuesto.objects.order_by('impuesto')
	context_object_name = 'impuesto'
	paginate_by = 10
