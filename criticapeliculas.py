import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns


def mediapond(datos):
    suma=0
    for i in range (len(datos["Cantidad de volantes (Ni)"])):
        suma+= datos["Cantidad de volantes (Ni)"][i]*datos["Opinion xi"][i]
    
    num=0
    for i in datos["Cantidad de volantes (Ni)"]:
        num+=i

    return suma/num
