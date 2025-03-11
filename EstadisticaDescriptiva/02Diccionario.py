# Crear una funcion que se encargue de recibir un diccionario de las notas de los estudiantes de 
# analisis de datos que vana reprobar y obtener su min, max, media, y desviación estandar

import pandas as pd

def Estadisticas_notas(notas):
    notas = pd.Series(notas)
    estadistica = pd.Series( [notas.min(), notas.max(), notas.mean(), notas.std()], index = ['Min', 'Max', 'Media', 'Desviación Estándar'] )
    
    return estadistica
    
def Aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 6].sort_values(ascending = False)
    
    
notas = {'Juan': 9, 
         'Juanita': 8.3,
         'Pedro': 6.9, 
         'Rosalba': 5, 
         'Fede': 4.5, 
         'Beto': 7.5 }

print( Estadisticas_notas(notas) )
print( Aprobados(notas) )
