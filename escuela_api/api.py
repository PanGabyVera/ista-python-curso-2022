from flask import Flask, jsonify, request
from email import message
from hashlib import new
import json
from analisis import Lector 
import reporte_asistencia

app = Flask(__name__)

def lectura():
    return reporte_asistencia.asistencias_completas()

@api.route('/Listar')
def procesar_informacion():
    contenido = lectura()()
    return jsonify(contenido)