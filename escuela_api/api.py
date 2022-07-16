from flask import Flask, jsonify, request
from email import message
from hashlib import new
import json
from analisis.reportes.reporte_asistencia import asistencias_completas, estudiante_id, estudiante_ISTA, leer_estudiante, leer_asistencia

api = Flask(__name__)



@api.route('/')
def home():
    return "Bienvenido al crud de asistencia de alumnos"


@api.route('/listar/Completa')
def procesar_informacion():
    contenido = asistencias_completas().to_json()
    return jsonify(contenido)


@api.route('/listar/ISTA')
def lista_ista():
    contenido = estudiante_ISTA().to_json()
    return jsonify(contenido)
    

@api.route('/listar/Estudiantes')
def lista_est():
    contenido = leer_estudiante().to_json()
    return jsonify(contenido)


@api.route('/listar/Asistencia')
def lista_asi():
    contenido = leer_asistencia().to_json()
    return jsonify(contenido)


@api.route('/listar/id')
def lista_id(id):
    contenido = estudiante_id(id).to_json()
    return jsonify(contenido)


if __name__ == '__main__':
    api.run(debug=True, port=5000)
