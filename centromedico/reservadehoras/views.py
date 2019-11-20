from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from reservadehoras.models import Sucursal, Cliente
""" 
EJEMPLO	
	def index(request):
    	listado = Pregunta.objects.order_by('-fecha_publicacion')[:10]
    	template = loader.get_template('encuestas/index.html')
    	context = {
        'listado': listado,
    }
    return HttpResponse(template.render(context, request))
"""
def IngreseRut(request):
    pagina = loader.get_template('reservadehoras/IngreseRut.html')
    context = {'Cliente': Cliente.rut, }
    return HttpResponse(pagina.render(context, request))



def MenuPrincipal(request):
    pagina = loader.get_template('reservadehoras/MenuPrincipal.html')
    context = {'Cliente': Cliente.rut, }
    return HttpResponse(pagina.render(context, request))