import pandas as pd
import csv 

asi = pd.read_csv("datos/asistencia.csv")
est = pd.read_csv("datos/estudiante.csv")

# print(estudiante.sort_values(by= 'primer_apellido')) #de orden menor a mayor
# print(estudiante.sort_values(by= 'primer_apellido', ascending=False)) #de orden mayor a menor

aa = pd.DataFrame(asi)
ba = pd.DataFrame(est)

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
    return result



   