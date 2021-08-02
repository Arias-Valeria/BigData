import pymysql
import numpy as np
import pandas as pd
from matplotlib import style
from matplotlib import pyplot as plt

conexion = pymysql.connect(host = "localhost", user = "root", password = "D1str3$$*", database = "tarifas")
miCursor = conexion.cursor()
miCursor.execute("SELECT ï»¿zona_inyeccion, volumetrica FROM sumasTarifa")
result = miCursor.fetchall

zona_inyeccion = []
volumetrica = []

for i in miCursor:
    zona_inyeccion.append(i[0])
    volumetrica.append(i[1])

plt.bar(zona_inyeccion, volumetrica)
plt.ylim(0, 150)
plt.xlabel("Zona de extracción")
plt.ylabel("Volumétrica")
plt.show()

#data = pd.read_csv('tarifas.csv', encoding = 'utf-8').fillna(0)
#x = data['zona_inyeccion'].iloc[0:10].values
#print(x)

#figura = plt.figure ()
#axes = figura.add_subplot(1,1,1)
#axes.plot([1,2,3,4], [3,5,7,25])
#plt.show()
#cursor.execute()

#Obtener los datos de la bse de datos.

print(conexion)
