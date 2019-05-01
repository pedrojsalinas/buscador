from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rdflib.serializer import Serializer
from django.views import View
import rdflib

# clase del buscador
class BuscadorView(View):
    # metodo que limpia los datos y retorna diccionario con datos
    def consulta(self, palabra):
        g = rdflib.Graph()
        g.parse("emancipada.rdf")
        # diccionario vacio
        datos = {}
        # consulta que obtiene sujeto, predicado y objeto
        query = 'SELECT ?s ?p ?o  WHERE { ?s ?p ?o .FILTER regex(str(?s), "%s") .}' % (
            palabra.title())
        for row in g.query(query):
            sujeto = row.s.split("/")
            predicado = row.p.split("/")
            objeto = row.o.split("/")
            predicado = predicado[-1].split("#")[-1]
            objeto = objeto[-1].split("#")[-1]
            # agrega datos al diccionario
            datos[predicado] = objeto
        # comprueba si retorna datos
        if (len(datos)==0):
            datos = {'mensaje': 'No hay datos.'}
        return datos


    # metodo get obtiene solicitud del cliente
    def get(self, request):
        # comprueba si es una solicitud GET
        if request.method == 'GET':
            # parametro de la solicitud web
            query = request.GET['consulta']
            # llama a metodo consulta
            datos = self.consulta(query)
            # retorna json con los datos obtenidos
            return JsonResponse(datos)
