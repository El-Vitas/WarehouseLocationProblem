import random
from config import *

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
                
def crearTxt(instancia: Instancia,cont):
    txt = ""
    n_ubicaciones_I_C = len(instancia.get_ubicaciones_I_C())
    n_ubicaciones_I_V = len(instancia.get_ubicaciones_I_V())
    n_ubicaciones_J = len(instancia.get_ubicaciones_J())

    txt+= f"NC = {n_ubicaciones_I_C};\n" #numero de celestes
    txt+= f"NVC = {n_ubicaciones_I_V};\n" #numero de verde claro
    txt+= f"NJ = {n_ubicaciones_J};\n\n" #numero de bodegas

    txt+= "C_I_C = [" # COSTO INSTALACION CELESTE
    for i in range(n_ubicaciones_I_C):
        txt+= str(instancia.get_costos_instalacion_C()[i])
        if i < n_ubicaciones_I_C - 1:
            txt+= ", "
        else:
            txt+= "];\n\n" 

    txt+= "C_I_VC = [" #COSTO INSTALACION VERDE CLARO
    for i in range(n_ubicaciones_I_V):
        txt+= str(instancia.get_costos_instalacion_V()[i])
        if i < n_ubicaciones_I_V - 1:
            txt+= ", "
        else:
            txt+= "];\n\n" 

    txt+= "C_B_C = [" #CAPACIDAD BODEGAS CELESTE
    for i in range(n_ubicaciones_I_C):
        txt+= str(instancia.get_capacidad_bodegas_C()[i])
        if i < n_ubicaciones_I_C - 1:
            txt+= ", "
        else:
            txt+= "];\n\n" 

    txt+= "C_B_VC = [" #CAPACIDAD BODEGAS VERDE CLARO
    for i in range(n_ubicaciones_I_V):
        txt+= str(instancia.get_capacidad_bodegas_V()[i])
        if i < n_ubicaciones_I_V - 1:
            txt+= ", "
        else:
            txt+= "];\n\n" 
    
    txt+= "E_C = [" #EMISIONES CELESTE
    for i in range(n_ubicaciones_I_C):
        txt+= str(instancia.get_emisiones_operacion_C()[i])
        if i < n_ubicaciones_I_C - 1:
            txt+= ", "
        else:
            txt+= "];\n\n"

    txt+= "E_VC = [" #EMISIONES VERDE CLARO
    for i in range(n_ubicaciones_I_V):
        txt+= str(instancia.get_emisiones_operacion_V()[i])
        if i < n_ubicaciones_I_V - 1:
            txt+= ", "
        else:
            txt+= "];\n\n" 

    txt+= "D_C =\n" #DISTANCIA J A CELESTES
    for i in range(n_ubicaciones_I_C):
        if i == 0:
            txt+= "["
        txt+= "|"
        for j in range(n_ubicaciones_J):
            txt+= str(instancia.get_distancias_C()[i][j])
            if j < n_ubicaciones_J -1:
                txt+= ", "
            elif i < n_ubicaciones_I_C - 1 and j == n_ubicaciones_J -1:
                txt+= ",\n"
        if i == n_ubicaciones_I_C - 1:
            txt+= "|];\n\n"

    txt+= "D_VC =\n" #DISTANCIA J A VERDE CLARO
    for i in range(n_ubicaciones_I_V):
        if i == 0:
            txt+= "["
        txt+= "|"
        for j in range(n_ubicaciones_J):
            txt+= str(instancia.get_distancias_V()[i][j])
            if j < n_ubicaciones_J -1:
                txt+= ", "
            elif i < n_ubicaciones_I_V - 1 and j == n_ubicaciones_J -1:
                txt+= ",\n"
        if i == n_ubicaciones_I_V - 1:
            txt+= "|];\n\n"

    txt+= "int: NC;\n"
    txt+= "int: NVC;\n"
    txt+= "int: NJ;\n"
    txt+= "array[1..NC] of int: C_I_C;\n"
    txt+= "array[1..NVC] of int: C_I_VC;\n"
    txt+= "array[1..NC] of int: C_B_C;\n"
    txt+= "array[1..NVC] of int: C_B_VC;\n"
    txt+= "array[1..NC] of int: E_C;\n"
    txt+= "array[1..NVC] of int: E_VC;\n"
    txt+= "array[1..NC,1..NJ] of int: D_C;\n"
    txt+= "array[1..NVC,1..NJ] of int: D_VC;\n"

    txt+= "array[1..NC,1..NJ] of var 0..1: X_C;\n"
    txt+= "array[1..NVC,1..NJ] of var 0..1: X_VC;\n" 
    txt+= "array[1..NC] of var 0..1: Y_C;\n" 
    txt+= "array[1..NVC] of var 0..1: Y_VC;\n\n"

    txt+= "constraint sum(i in 1..NC, j in 1..NJ) (X_C[i, j] * D_C[i, j] * 1.5) + sum(i in 1..NVC, j in 1..NJ) (X_VC[i, j] * D_VC[i, j] * 1.5) + sum(i in 1..NC) (C_I_C[i] * Y_C[i]) + sum(i in 1..NVC) (C_I_VC[i] * Y_VC[i]) <= 6000 * NJ;\n\n";
    txt+= "constraint forall(i in 1..NC, j in 1..NJ) (X_C[i, j] <= Y_C[i]);\n\n"
    txt+= "constraint forall(i in 1..NVC, j in 1..NJ) (X_VC[i, j] <= Y_VC[i]);\n\n"
    txt+= "constraint forall(j in 1..NJ) (sum(i in 1..NC) (X_C[i, j]) + sum(i in 1..NVC) (X_VC[i, j]) = 1);\n\n"
    txt+= "constraint forall(i in 1..NC) (sum(j in 1..NJ) (X_C[i, j]) <= C_B_C[i]);\n\n"
    txt+= "constraint forall(i in 1..NVC) (sum(j in 1..NJ) (X_VC[i, j]) <= C_B_VC[i]);\n\n"

    txt+= "constraint sum(i in 1..NVC) (Y_VC[i]) >= 0.40 * NVC;\n\n"
    txt+= "constraint sum(i in 1..NC) (Y_C[i]) >= 0.40 * NC;\n\n"

    txt+= "solve minimize sum(i in 1..NC, j in 1..NJ) (X_C[i, j] * D_C[i, j] * 1.5) + sum(i in 1..NVC, j in 1..NJ) (X_VC[i, j] * D_VC[i, j] * 1.5) + sum(i in 1..NC) (E_C[i] * Y_C[i]) + sum(i in 1..NVC) (E_VC[i] * Y_VC[i]);\n\n";

    txt+= 'output ["FO = ", show(sum(i in 1..NC, j in 1..NJ) (X_C[i, j] * D_C[i, j] * 1.5) + sum(i in 1..NVC, j in 1..NJ) (X_VC[i, j] * D_VC[i, j] * 1.5) + sum(i in 1..NC) (E_C[i] * Y_C[i]) + sum(i in 1..NVC) (E_VC[i] * Y_VC[i]))];\n'

    mzn = open(f"modelo_minizinc{cont}.mzn","w")
    mzn.write(txt)
    mzn.close()

    return
