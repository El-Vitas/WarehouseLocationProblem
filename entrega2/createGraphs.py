import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def create_graphs():
    datos = []
    nombre_archivo = 'datos.txt'
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            elementos = [float(e) for e in linea.strip().split()]
            tupla = tuple(elementos)
            datos.append(tupla)

    datos_ordenados = sorted(datos, key=lambda x: x[0])
    obj = [t[0] for t in datos_ordenados]
    times = [t[1] for t in datos_ordenados]

    #grafico de dispersion de funcion objetivo vs tiempo
    plt.figure(figsize=(10, 6))
    plt.scatter(obj, times, marker='o', label='Datos', linestyle='-', alpha=0.1)
    plt.ylabel('Tiempo (s)')
    plt.xlabel('Valores de F.O.')
    plt.title('F.O. vs. Tiempo (Gráfico de líneas suavizado)')
    plt.grid(True)
    plt.legend()
    plt.show()

    datos_ordenados = sorted(datos, key=lambda x: x[2])
    ubicacionesI = [t[2] for t in datos_ordenados]
    times = [t[1] for t in datos_ordenados]

    df = pd.DataFrame({'UbicacionesI': ubicacionesI, 'Tiempo': times})

    datos_agrupados = df.groupby('UbicacionesI')['Tiempo'].mean().reset_index()

    #plot con agrupando ubicaciones I y promediando el tiempo
    plt.figure(figsize=(10, 6))
    plt.plot(datos_agrupados['UbicacionesI'], datos_agrupados['Tiempo'], marker='o', label='Datos promediados')
    plt.ylabel('Tiempo promedio (s)')
    plt.xlabel('N ubicaciones I')
    plt.title('N ubicaciones I vs. Tiempo (Promedio)')
    plt.grid(True)
    plt.legend()
    plt.show()

    datos_ordenados = sorted(datos, key=lambda x: x[3])
    ubicacionesJ = [t[3] for t in datos_ordenados]
    times = [t[1] for t in datos_ordenados]

    df = pd.DataFrame({'UbicacionesJ': ubicacionesJ, 'Tiempo': times})

    datos_agrupados = df.groupby('UbicacionesJ')['Tiempo'].mean().reset_index()

    #plot con agrupando ubicaciones J y promediando el tiempo
    plt.figure(figsize=(10, 6))
    plt.plot(datos_agrupados['UbicacionesJ'], datos_agrupados['Tiempo'], marker='o', label='Datos promediados')
    plt.ylabel('Tiempo (s)')
    plt.xlabel('N Tiendas')
    plt.title('N tiendas. vs. Tiempo')
    plt.grid(True)
    plt.legend()
    plt.show()

    datos_ordenados = sorted(datos, key=lambda x: x[4])
    instancia = [t[4] for t in datos_ordenados]
    times = [t[1] for t in datos_ordenados]

    df = pd.DataFrame({'Instancia': instancia, 'Tiempo': times})

    datos_agrupados = df.groupby('Instancia')['Tiempo'].mean().reset_index()

    # Grafico de barra agrupados por instancias con el tiempo promedio
    plt.figure(figsize=(10, 6))
    plt.bar(datos_agrupados['Instancia'], datos_agrupados['Tiempo'], color='blue', alpha=0.7, label='Promedio de Tiempo')
    plt.xlabel('N Instancia')
    plt.ylabel('Tiempo promedio (s)')
    plt.title('N Instancia vs. Tiempo (Promedio)')
    plt.xticks(range(1, 16))  # Establecer el eje x como valores enteros del 1 al 15
    plt.grid(True)
    plt.legend()
    plt.show()

