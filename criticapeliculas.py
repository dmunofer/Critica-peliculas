import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
from math import sqrt


def mediapond(datos):
    suma=0
    for i in range (len(datos["Cantidad de volantes (Ni)"])):
        suma+= datos["Cantidad de volantes (Ni)"][i]*datos["Opinion xi"][i]
    
    num=0
    for i in datos["Cantidad de volantes (Ni)"]:
        num+=i

    return suma/num

def varianza(datos):
    cont=0
    for i in datos["Ni*((xi-media)^2)"]:
        cont+=i

    return cont/sum(datos["Cantidad de volantes (Ni)"])


def porcentaje(datos):

    print("el 68% de los datos estan entre:"+ mediapond(datos)-sqrt(varianza(datos))+ "y"+ mediapond(datos)+sqrt(varianza(datos)))
    print("el 95% de los datos estan entre:"+ mediapond(datos)-2*sqrt(varianza(datos))+ "y"+ mediapond(datos)+2*sqrt(varianza(datos)))
    print("el 99.7% de los datos estan entre:"+ mediapond(datos)-3*sqrt(varianza(datos))+ "y"+ mediapond(datos)+3*sqrt(varianza(datos)))

