import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Variable independiente(Altura)
altura = [181, 172, 178, 169, 180, 178, 173, 165, 175, 175, 165, 178, 165, 171, 173, 167, 165, 164, 170, 164, 180, 183, 167, 180, 170, 170, 172, 162, 155, 170, 172, 160, 180, 158, 180, 185, 182, 169, 157]

# Variable dependiente(Peso)
peso = [90, 70, 65, 59, 98, 85, 56, 58, 79, 84, 48, 76, 51, 65, 89, 55, 86, 60, 80, 69, 65, 105, 74, 80, 60, 87, 97, 58, 56, 78, 72, 120, 92, 62, 75, 83, 77, 68, 49]

# Dataframe para los datos
df = pd.DataFrame({
    "Altura": altura,
    "Peso": peso
})

# Calculos necesarios para la regresion
df["x*y"] = df["Altura"] * df["Peso"]
df["x^2"] = df["Altura"] ** 2
df["y^2"] = df["Peso"] ** 2

# Muestro la Tabla creada 
print("\nTABLA DE DATOS\n")
print(df)

n = len(df) #Guardo la cantidad de filas que tiene el DataFrame

# Sumatorias necesarias para la regresion
sumatoria_x = df["Altura"].sum() 
sumatoria_y = df["Peso"].sum()
sumatoria_xy = df["x*y"].sum()
sumatoria_x2 = df["x^2"].sum()
sumatoria_y2 = df["y^2"].sum()

# Muestro las sumatorias
print("\nSUMATORIAS\n")

print("Suma X:", sumatoria_x)
print("Suma Y:", sumatoria_y)
print("Suma XY:", sumatoria_xy)
print("Suma X^2:", sumatoria_x2)
print("Suma Y^2:", sumatoria_y2)

# Fórmula de (b)
b = ((n * sumatoria_xy) - (sumatoria_x * sumatoria_y)) / ((n * sumatoria_x2) - (sumatoria_x ** 2))

# Fórmula de (a)
a = ((sumatoria_y * sumatoria_x2) - (sumatoria_xy * sumatoria_x)) / ((n * sumatoria_x2) - (sumatoria_x ** 2))

print("\nRECTA DE REGRESION\n")

print(f"y = {a:.2f} + {b:.2f}x")

# Formula de (r)
r = ((n * sumatoria_xy) - (sumatoria_x * sumatoria_y)) / np.sqrt(((n * sumatoria_x2) - (sumatoria_x ** 2)) * ((n * sumatoria_y2) - (sumatoria_y ** 2)))

print("\nCORRELACION\n")

print(f"r = {r:.4f}")

# Formula de (r²)
r2 = r ** 2

print(f"r^2 = {r2:.4f}")

# Interpretaciones
if r > 0:
    print("\nLa correlación es positiva.")
elif r < 0:
    print("\nLa correlación es negativa.")
else:
    print("\nNo existe correlación.")

print(f"El modelo explica aproximadamente el {r2 * 100:.2f}% de la variabilidad.")

# GRAFICO
# Valores para la recta
x = np.array(altura)
y = a + b * x

plt.scatter(altura, peso)
plt.plot(x, y)

plt.title("Regresión Lineal")
plt.xlabel("Altura")
plt.ylabel("Peso")

plt.show()