import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')

# a) La tabla
def calcular_estadisticas(df):
    numeric_cols = df.select_dtypes(include=['number']).columns
    stats_results = {}
    for col in numeric_cols:
        data = df[col].dropna()
        stats_results[col] = {
            "Media": data.mean(),
            "Mediana": data.median(),
            "Moda": data.mode().tolist(),
            "Rango": data.max() - data.min(),
            "Varianza": data.var(),
            "Desviación Estándar": data.std()
        }
    return pd.DataFrame(stats_results)

print( calcular_estadisticas(df) )


# b) La gráfica
df_sample = df.head(2000)

plt.figure(figsize=(10, 5))

plt.bar(df_sample.index, df_sample['median_house_value'], label="Valor medio de la casa", color='blue')
plt.bar(df_sample.index, df_sample['population'] * 10, label="Población", color='red')

promedio_casa = df['median_house_value'].mean()
plt.axhline(promedio_casa, color='orange', linestyle='-', linewidth = 3, label="Promedio del valor de la casa")

plt.xlabel("Población")
plt.ylabel("Valor medio de la casa")
plt.title("Grafica de Barras del Valor Medio de la Casa VS la Población")

plt.show()