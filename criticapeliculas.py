import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
from math import sqrt

datos = pd.DataFrame({"Opinion xi": [5,4,3,2,1,0], "Cantidad de volantes (Ni)": [40,99,145,133,96,40],"Productos(Ni*xi)": [200,396,435,266,96,0], "Ni*((xi-media)^2)":[246.21,217.14,33.54,35.82,221.50,253.81]})


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


def plot(datos):
    plt.figure(figsize=((15,15)))
    sns.lineplot(data=datos, x = "Opinion xi", y="Cantidad de volantes (Ni)", color = "Blue")


def critica():
    mediapond(datos)
    varianza(datos)
    sqrt(varianza(datos))
    porcentaje(mediapond(datos), sqrt(varianza(datos)))
    plot(datos)