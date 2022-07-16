import pandas as pd

asi = pd.read_csv("escuela_api/datos/asistencia.csv")
est = pd.read_csv("escuela_api/datos/estudiante.csv")

# print(estudiante.sort_values(by= 'primer_apellido')) #de orden menor a mayor
# print(estudiante.sort_values(by= 'primer_apellido', ascending=False)) #de orden mayor a menor

aa = pd.DataFrame(asi)
ba = pd.DataFrame(est)

#aa = aa.to_json()
#ba = ba.to_json()

result = pd.merge(aa, ba, how="left")

def leer_asistencia():
    arc = None
    with open("datos/asistencia.csv") as a:
        arc = a.readlines()
    return arc


def leer_estudiante():
    dat = None
    with open("datos/estudiante.csv") as a:
        dat = a.readlines()
    return dat

def asistencias_completas():
    result = pd.merge(aa, ba, how="left")
    #result = result.to_json()
    return result

#para buscar solo al estudiante Ista
def estudiante_ISTA():
    estudiante_ista=pd.DataFrame(asistencias_completas().loc[asistencias_completas()['cedula']== 1106137229,['cedula','materia','fecha_año','fecha_mes','fecha_dia','primer_apellido','segundo_apellido','primer_nombre','segundo_nombre']])
    return estudiante_ista
   

def estudiante_id(id):
    estu_id = pd.DataFrame(asistencias_completas().loc[asistencias_completas()['cedula']== id,['cedula','materia','fecha_año','fecha_mes','fecha_dia','primer_apellido','segundo_apellido','primer_nombre','segundo_nombre']])
    return print(estu_id)

    estudiante_id(1150203440)