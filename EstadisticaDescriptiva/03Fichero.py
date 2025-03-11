# Vamos a hacer un ejemplo de carga de archivo y aplicar min, max, media y desviacion estandar

import pandas as pd

def Cotizacion(fichero):
    df = pd.read_csv( fichero, sep = ';', decimal = ',', thousands = '.', index_col = 0 )
    
    return pd.DataFrame( [ df.min, df.max, df.mean, df.std ], index = [ 'Minimo', 'Maximo', 'Media', 'Desviación Estándar' ] )

print( Cotizacion('./EstadisticaDescriptiva/cotizacion.csv') )