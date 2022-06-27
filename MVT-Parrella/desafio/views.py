from django.http import HttpResponse
from django.shortcuts import render
from desafio.models import Fam
from django.template import loader

# Create your views here.
def inicio(request):
    return HttpResponse('<h1>Él mato a un policia bondiolizado</h1>')

def plantilla(request):
    return render(request, 'prueba.html')

def desafio(request,name,age):
    familiar = Fam(nombre=name,edad=age)
    familiar.save()
    return render(request, 'modelo.html', {'familiar': familiar})

def listado_fam(request):
    template = loader.get_template('listado.html')
    
    lista_fam = Fam.objects.all()
    
    render = template.render({'lista_fam': lista_fam})
    return HttpResponse(render)
