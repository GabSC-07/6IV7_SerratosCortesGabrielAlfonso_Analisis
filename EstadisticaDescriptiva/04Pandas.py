import pandas as pd
import matplotlib.pyplot as plt     #pip install matplotlib

df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')

# Mostrar las primeras 5 filas
print( df.head() )

# Las ultimas 5 filas
print( df.tail() )

# Una fila en especifico
print( df.iloc[7] )

# Mostrar una columna por su nombre
print( df["ocean_proximity"])

# Obtener la media de la columna de total de cuartos
media_cuartos = df["total_rooms"].mean()
print('Media de cuartos: ', media_cuartos)

# Obtener la mediana de la columa population
medaiana_pobacion = df["population"].median()
print('Mediana de population: ', medaiana_pobacion)

std_age = df["housing_median_age"].std()
print('Desviacion Estandar de años: ', std_age)

# Para poder filtrar
filtro_oceano = df[ df["ocean_proximity"] == "ISLAND" ]
print('Filtro de proximidad del océano: ', filtro_oceano) 

# Vaamos a crear un grafico de dispersion entere lsoregistros de la proximidad del oceano vs lso precios
plt.scatter( df["ocean_proximity"][:10], df["median_house_value"][:10])

# Hay que definir a X y Y
plt.xlabel('Proximidad')
plt.ylabel('Precio')

plt.title('Gráfico de Dispersion de Proximidad al oceano vs Precio')
plt.show()

