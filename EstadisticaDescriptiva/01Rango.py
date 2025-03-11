# Vamos a crear un programa que pregunte al usuario por las ventas de un rango de años y 
# muestre por pantalla una serie de datos de las ventas indexidas por lo años antes y 
# despues de aplicar un descuento del 10%

import pandas as pd

inicio = int( input('Introduce el año inicial de ventas: ') )
fin = int( input('Introduce el año finald de ventas: ') )

ventas = {}

for i in range(inicio, fin + 1):
    ventas[i] = float( input('Introduce las ventas del año ' + str(i) + ': ') )
    
ventas = pd.Series(ventas)
print('Ventas \n', ventas)
print('Ventas con Descuento \n', ventas * 0.9)

 