import datetime
import imp
from django.template import Template, Context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

temasDelCurso = ["Plantillas", "Modelos", "Formularios", "Despliegue de Aplicación"]
def saludo(request): # PRIMERA VISTA

    nombre = "Juan"
    apellido = "Díaz"
    ahora = datetime.datetime.now()

    #doc_externo = open(r'C:\Users\Lautaro.DESKTOP-PFAUVN7\Desktop\Proyecto Django\Proyecto1\Plantillas\miplantilla.html')
    #plt = Template(doc_externo.read()) # CREACIÓN OBJETO TIPO TEMPLATE
    #doc_externo.close()

    #doc_externo = loader.get_template('miplantilla.html')

    #ctx = Context({"nombre_persona": nombre, "apellido_persona": apellido, "fecha_actual": ahora, "temas": temasDelCurso}) # CREACIÓN DEL CONTEXTO

    #documento = doc_externo.render({"nombre_persona": nombre, "apellido_persona": apellido, "fecha_actual": ahora, "temas": temasDelCurso}) # RENDERIZADO DEL OBJETO TEMPLATE
    
    return render(request, "miplantilla.html", {"nombre_persona": nombre, "apellido_persona": apellido, "fecha_actual": ahora, "temas": temasDelCurso})

def despedida(request):

    return HttpResponse("Hasta luego alumnos")

def dameFecha(request):

    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" %fecha_actual
    return HttpResponse(documento)

def calculaEdad(request, edad, agno): # VISTA CON PASO DE PARÁMETROS

    #edadActual = 18
    periodo = agno - 2022
    edadFutura = edad + periodo
    documento = """<html>
    <body>
    <h2>
    En el año %s tendrás %s años
    </h2>
    </body>
    </html>"""%(agno, edadFutura)
    return HttpResponse(documento)
