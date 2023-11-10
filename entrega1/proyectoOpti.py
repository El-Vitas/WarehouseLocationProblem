import random
import csv

# Rangos para generar ubicaciones I y J
INSTANCIAS = (
    ((5, 7), (6, 10)),
    ((8, 12), (10, 20)),
    ((13, 18), (20, 30)),
    ((19, 23), (30, 40)),
    ((24, 30), (40, 50)),
    ((32, 38), (50, 65)),
    ((39, 45), (65, 80)),
    ((46, 53), (80, 95)),
    ((54, 65), (95, 110)),
    ((66, 72), (110, 125)),
    ((72, 81), (125, 145)),
    ((82, 91), (145, 165)),
    ((92, 101), (165, 185)),
    ((102, 111), (185, 205)),
    ((112, 131), (205, 225))
)

# Rangos para ubicaciones I celestes (C), verdes claros (VC) y verde oscuro (VO)
RANGOC1 = (1, 99, 1, 500)
RANGOC2 = (100, 600, 1, 99)
RANGOC3 = (501, 600, 100, 600)
RANGOC4 = (1, 500, 501, 600)

RANGOVC1 = (100, 224, 100, 375)
RANGOVC2 = (225, 500, 100, 224)
RANGOVC3 = (376, 500, 225, 500)
RANGOVC4 = (100, 375, 376, 500)

RANGOVO = (225, 375, 225, 375)


class Instancia:
    """
    Descripción: Clase que representa una instancia con información sobre ubicaciones, costos, capacidad y emisiones.
    """
    def __init__(self):
        self.ubicaciones_I_C = []
        self.ubicaciones_I_V = []
        self.ubicaciones_J = []
        self.costos_instalacion_C = []
        self.costos_instalacion_V = []
        self.capacidad_bodegas_C = []
        self.capacidad_bodegas_V = []
        self.emisiones_operacion_C = []
        self.emisiones_operacion_V = []
        self.distancias_C = []
        self.distancias_V = []

    def get_ubicaciones_I_C(self):
        return self.ubicaciones_I_C

    def append_ubicaciones_I_C(self, nueva_ubicacion_I_C):
        self.ubicaciones_I_C.append(nueva_ubicacion_I_C)

    def get_ubicaciones_I_V(self):
        return self.ubicaciones_I_V

    def append_ubicaciones_I_V(self, nueva_ubicacion_I_V):
        self.ubicaciones_I_V.append(nueva_ubicacion_I_V)

    def get_ubicaciones_J(self):
        return self.ubicaciones_J

    def append_ubicaciones_J(self, nueva_ubicacion_J):
        self.ubicaciones_J.append(nueva_ubicacion_J)

    def get_costos_instalacion_C(self):
        return self.costos_instalacion_C

    def append_costos_instalacion_C(self, nuevo_costo_instalacion_C):
        self.costos_instalacion_C.append(nuevo_costo_instalacion_C)

    def get_costos_instalacion_V(self):
        return self.costos_instalacion_V

    def append_costos_instalacion_V(self, nuevo_costo_instalacion_V):
        self.costos_instalacion_V.append(nuevo_costo_instalacion_V)

    def get_capacidad_bodegas_C(self):
        return self.capacidad_bodegas_C

    def append_capacidad_bodegas_C(self, nueva_capacidad_bodegas_C):
        self.capacidad_bodegas_C.append(nueva_capacidad_bodegas_C)

    def get_capacidad_bodegas_V(self):
        return self.capacidad_bodegas_V

    def append_capacidad_bodegas_V(self, nueva_capacidad_bodegas_V):
        self.capacidad_bodegas_V.append(nueva_capacidad_bodegas_V)

    def get_emisiones_operacion_C(self):
        return self.emisiones_operacion_C

    def append_emisiones_operacion_C(self, nueva_emision_operacion_C):
        self.emisiones_operacion_C.append(nueva_emision_operacion_C)

    def get_emisiones_operacion_V(self):
        return self.emisiones_operacion_V

    def append_emisiones_operacion_V(self, nueva_emision_operacion_V):
        self.emisiones_operacion_V.append(nueva_emision_operacion_V)

    def get_distancias_C(self):
        return self.distancias_C

    def append_distancias_C(self, nueva_distancia_C):
        self.distancias_C.append(nueva_distancia_C)

    def get_distancias_V(self):
        return self.distancias_V

    def append_distancias_V(self, nueva_distancia_V):
        self.distancias_V.append(nueva_distancia_V)


def crearCoordenadas(n_ubicaciones_I, n_ubicaciones_J, instancia: Instancia):
    """
    Descripción: Crea coordenadas aleatorias para las ubicaciones I y J de una instancia.

    Parametros:
        n_ubicaciones_I (int): Número de ubicaciones I a crear.
        n_ubicaciones_J (int): Número de ubicaciones J a crear.
        instancia (Instancia): La instancia en la que se agregarán las ubicaciones generadas.

    Retorna:
        No tiene retorno explícito, ya que la función modifica la instancia proporcionada.
    """
    i = 0
    while i < n_ubicaciones_I:
        opciones = [RANGOC1, RANGOC2, RANGOC3, RANGOC4, RANGOVC1, RANGOVC2, RANGOVC3, RANGOVC4]
        rango_elegido = random.choice(opciones)
        index = opciones.index(rango_elegido)

        x = random.randint(rango_elegido[0], rango_elegido[1])
        y = random.randint(rango_elegido[2], rango_elegido[3])

        if index in [0,1,2,3]:      
            if ((x, y) not in instancia.get_ubicaciones_I_C()):
                instancia.append_ubicaciones_I_C((x, y))
                i += 1
        else:
            if ((x, y) not in instancia.get_ubicaciones_I_V()):
                instancia.append_ubicaciones_I_V((x, y))
                i += 1
    i = 0
    while i < n_ubicaciones_J:
        x = random.randint(RANGOVO[0], RANGOVO[1])
        y = random.randint(RANGOVO[2], RANGOVO[3])
        if ((x, y) not in instancia.get_ubicaciones_J()):
            instancia.append_ubicaciones_J((x, y))
            i += 1

def calcularDistancias(n_ubicaciones_J, instancia: Instancia, i, ubicaciones_I):
    """
    Descripción: Calcula las distancias entre una ubicación I entregada y todas las ubicaciones J.

    Parámetros:
        n_ubicaciones_J (int): Número de ubicaciones J.
        instancia (Instancia): Instancia que contiene los datos de ubicaciones entregadas.
        i (int): Índice de la ubicación I que se va a calcular.
        ubicaciones_I (list): Lista de coordenadas de ubicaciones I.

    Retorna:
        fila: Lista de distancias entre la ubicación I y todas las ubicaciones J.
    """
    fila = []
    for j in range(n_ubicaciones_J):
        deltaX = ubicaciones_I[i][0] - (instancia.get_ubicaciones_J())[j][0]
        deltaY = ubicaciones_I[i][1] - (instancia.get_ubicaciones_J())[j][1]
        distancia = round((((deltaX) ** 2) + ((deltaY) ** 2)) ** (1/2))
        fila.append(distancia)
    return fila

def calcularValores(instancia: Instancia, n_ubicaciones_J):
    """
    Descripción: Calcula y asigna valores aleatorios a costos, capacidad y emisiones para ubicaciones I.

    Parámetros:
        instancia (Instancia): Instancia que contiene los datos de ubicaciones.
        n_ubicaciones_J (int): Número de ubicaciones J.
    """
    def calcularValoresParaTipo(instancia: Instancia, n_ubicaciones_J, tipo):
        """
        Descripción: Calcula y agrega valores de distancia, costos, capacidad y emisiones para las ubicaciones de un tipo específico (celeste o verde claro) de la instancia.

        Parametros:
            instancia (Instancia): La instancia en la que se agregarán los valores calculados.
            n_ubicaciones_J (int): Número de ubicaciones J.
            tipo (str): El tipo de ubicaciones a calcular ('C' para celeste, 'V' para verde claro).

        Retorna:
            No tiene retorno explícito, ya que la función modifica la instancia proporcionada.
        """
        ubicaciones_I = ( instancia.get_ubicaciones_I_C() if tipo == 'C' else instancia.get_ubicaciones_I_V() )

        for i in range(len(ubicaciones_I)):
            distancia = calcularDistancias(n_ubicaciones_J, instancia, i, ubicaciones_I)
            costos = random.randint(1000, 3000)
            capacidad = random.randint(2, round(n_ubicaciones_J/3))
            emisiones = random.randint(20, 70)

            if tipo == 'C':
                instancia.append_distancias_C(distancia)
                instancia.append_capacidad_bodegas_C(capacidad)
                instancia.append_costos_instalacion_C(costos)
                instancia.append_emisiones_operacion_C(emisiones)
            else:
                instancia.append_distancias_V(distancia)
                instancia.append_capacidad_bodegas_V(capacidad)
                instancia.append_costos_instalacion_V(costos)
                instancia.append_emisiones_operacion_V(emisiones)

    calcularValoresParaTipo(instancia, n_ubicaciones_J, "C")
    calcularValoresParaTipo(instancia, n_ubicaciones_J, "V")
                

def crearCSV(instancia: Instancia, escritor_csv, cont):
    """
    Descripción: Crea un archivo CSV con los datos de la instancia.

    Parámetros:
        instancia (Instancia): Instancia que contiene los datos de ubicaciones.
        escritor_csv (csv.writer): Escritor CSV para escribir en el archivo.
        cont (int): Número de instancia.
    """
    def escribir_seccion(titulo, etiqueta, datos, opcion):
        """
        Descripción: Escribe una sección en el archivo CSV con un título, etiquetas, y datos.

        Parámetros:
            titulo (str): Título de la sección.
            etiqueta (list): Etiquetas para las columnas de datos.
            datos (list): Datos a escribir en la sección.
            opcion (int): Opción para determinar cómo escribir los datos (0 para una sola fila, 1 para múltiples filas).
        """
        escritor_csv.writerow([titulo])
        escritor_csv.writerow(etiqueta)
        if opcion == 0:
            escritor_csv.writerow(datos)
        else:
            for dato in datos:
                escritor_csv.writerow(dato)
        escritor_csv.writerow([])

    escritor_csv.writerow([f"Instancia: {cont}"])

    n_ubicaciones_I_C = len(instancia.get_ubicaciones_I_C())
    n_ubicaciones_I_V = len(instancia.get_ubicaciones_I_V())
    n_ubicaciones_J = len(instancia.get_ubicaciones_J())

    escribir_seccion("Ubicaciones I celestes (x,y):", [f"I_C{i}" for i in range(n_ubicaciones_I_C)], instancia.get_ubicaciones_I_C(), 0)
    escribir_seccion("Ubicaciones I verde claro (x,y):", [f"I_V{i}" for i in range(n_ubicaciones_I_V)], instancia.get_ubicaciones_I_V(), 0)
    escribir_seccion("Ubicaciones J (x,y):", [f"J{j}" for j in range(n_ubicaciones_J)], instancia.get_ubicaciones_J(), 0)
    escribir_seccion("Costos de instalación celeste (I):", [f"I_C{i}" for i in range(n_ubicaciones_I_C)], instancia.get_costos_instalacion_C(), 0)
    escribir_seccion("Costos de instalación verde claro (I):", [f"I_V{i}" for i in range(n_ubicaciones_I_V)], instancia.get_costos_instalacion_V(), 0)
    escribir_seccion("Capacidad de bodegas celeste (I):", [f"I_C{i}" for i in range(n_ubicaciones_I_C)], instancia.get_capacidad_bodegas_C(), 0)
    escribir_seccion("Capacidad de bodegas verde claro (I):", [f"I_V{i}" for i in range(n_ubicaciones_I_V)], instancia.get_capacidad_bodegas_V(), 0)
    escribir_seccion("Emisiones por operación celeste (I):", [f"I_C{i}" for i in range(n_ubicaciones_I_C)], instancia.get_emisiones_operacion_C(), 0)
    escribir_seccion("Emisiones por operación verde claro (I):", [f"I_V{i}" for i in range(n_ubicaciones_I_V)], instancia.get_emisiones_operacion_V(), 0)
    escribir_seccion("Distancia (J x I) I celeste:", ["-"] + [f"J{i}" for i in range(n_ubicaciones_J)], [[f"I_C{i}"] + fila for i, fila in enumerate(instancia.get_distancias_C())], 1)
    escribir_seccion("Distancia (J x I) I verde claro:", ["-"] + [f"J{i}" for i in range(n_ubicaciones_J)], [[f"I_V{i}"] + fila for i, fila in enumerate(instancia.get_distancias_V())], 1)

def main():
    """
    Descripción: Función principal para crear instancias y escribir los datos en un archivo CSV.
    """
    cont = 0
    archivo_csv = open("instancias.csv", mode="w", newline="")
    escritor_csv = csv.writer(archivo_csv, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for rango_bodegas, rango_tiendas in INSTANCIAS:
        n_ubicaciones_I = random.randint(rango_bodegas[0], rango_bodegas[1])
        n_ubicaciones_J = random.randint(rango_tiendas[0], rango_tiendas[1])
        instancia = Instancia()
        cont += 1

        crearCoordenadas(n_ubicaciones_I, n_ubicaciones_J, instancia)
        calcularValores(instancia, n_ubicaciones_J)
        crearCSV(instancia, escritor_csv, cont)

    archivo_csv.close()
    print("instancias.csv creado con exito.")

main()
