import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./Tareas/proyecto1.xlsx')

#  1: Ventas totales del comercio
ventas_totales = df["ventas_tot"].sum()
print(f"\n1. Ventas Totales: ${ventas_totales:,.2f}\n")

#  2: Adeudos
socios_con_adeudo = df[df["B_adeudo"] == "Con adeudo"]["no_clientes"].sum()
socios_sin_adeudo = df[df["B_adeudo"] == "Sin adeudo"]["no_clientes"].sum()
total_socios = socios_con_adeudo + socios_sin_adeudo
porcentaje_con_adeudo = (socios_con_adeudo / total_socios) * 100
porcentaje_sin_adeudo = (socios_sin_adeudo / total_socios) * 100
print(f"2. Socios con adeudo: {socios_con_adeudo} ({porcentaje_con_adeudo:.1f}%)")
print(f"   Socios sin adeudo: {socios_sin_adeudo} ({porcentaje_sin_adeudo:.1f}%)\n")

#  3: Grafica de ventas totales respecto al tiempo
df_fecha_ventas = df.groupby("B_mes")["ventas_tot"].sum()
plt.figure(figsize=(9, 5))
plt.bar(df_fecha_ventas.index, df_fecha_ventas.values, color="cyan")
plt.xlabel("Fecha")
plt.ylabel("Ventas Totales")
plt.title("Ventas Totales por Mes")
plt.show()

#  4: Gráfica de desviación estándar de los pagos contra el tiempo
df_std_pagos = df.groupby("B_mes")["pagos_tot"].std()
plt.figure(figsize=(10, 5))
plt.plot(df_std_pagos.index, df_std_pagos.values, marker="o", linestyle="-", color="#882EFA")
plt.xlabel("Fecha")
plt.ylabel("Desviación Estándar de Pagos")
plt.title("Variabilidad de los Pagos por Mes")
plt.show()

#  5: Deuda total de los clientes
deuda_total = df["adeudo_actual"].sum()
print(f"5. Deuda Total: ${deuda_total:,.2f}\n")

#  6: Porcentaje de la utilidad respecto al total de ventas
porcentaje_utilidad = ((ventas_totales - deuda_total) / ventas_totales) * 100
print(f"6. Porcentaje de Utilidad: {porcentaje_utilidad:.1f}%\n")

#  7: Gráfica de ventas por sucursal
df_ventas_sucursal = df.groupby("id_sucursal")["ventas_tot"].sum()
plt.figure(figsize=(8, 8))
plt.pie(df_ventas_sucursal, labels=df_ventas_sucursal.index, autopct="%1.1f%%", startangle=140)
plt.title("Distribución de Ventas por Sucursal")
plt.show()

#  8: Gráfica de deudas totales por sucursal contra el margen de utilidad
df_utilidad_sucursal = df.groupby("id_sucursal").agg({"ventas_tot": "sum", "adeudo_actual": "sum"})
df_utilidad_sucursal["margen_utilidad"] = df_utilidad_sucursal["ventas_tot"] - df_utilidad_sucursal["adeudo_actual"]

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df_utilidad_sucursal.index, df_utilidad_sucursal["adeudo_actual"], label="Deuda Total", color="#FA632E")
ax.bar(df_utilidad_sucursal.index, df_utilidad_sucursal["margen_utilidad"], label="Margen de Utilidad", color="#73FE57", bottom=df_utilidad_sucursal["adeudo_actual"][:30])
ax.set_xlabel("Sucursal")
ax.set_ylabel("Monto")
ax.set_title("Deuda Total vs Margen de Utilidad por Sucursal")
ax.legend()
plt.show()