import random
import threading
from minizinc import Instance, Model, Solver #pip install minizinc
from config import *
from createMZN import *

results = [i for i in range(len(INSTANCIAS))]
instancia_I = [i for i in range(len(INSTANCIAS))]
instancia_J = [i for i in range(len(INSTANCIAS))]
flag_error = False

def execute_mzn(modelo_mzn,cont):
    global results, flag_error
    model = Model(modelo_mzn)
    try:
        if flag_error:
            print("hola")
            return True
        solver = Solver.lookup("highs")
        instance = Instance(solver,model)
        result = instance.solve()

        if result.solution is not None:
            results[cont-1] = result

        else:
            print("No se encontro solucion.")
        
        return False

    except Exception as e:
        print("Error con el solver.")
        flag_error = True
        return flag_error

def create_instance(rango_bodegas, rango_tiendas,cont):
    global instancia_I, instancia_J
    n_ubicaciones_I = random.randint(rango_bodegas[0], rango_bodegas[1])
    n_ubicaciones_J = random.randint(rango_tiendas[0], rango_tiendas[1])
    instancia = Instancia()

    instancia_I[cont-1] = n_ubicaciones_I
    instancia_J[cont-1] = n_ubicaciones_J
    crearCoordenadas(n_ubicaciones_I, n_ubicaciones_J, instancia)
    calcularValores(instancia, n_ubicaciones_J)
    crearTxt(instancia,cont)


def write_data():
    global results, instancia_I,instancia_J
    with open('datos.txt', 'a') as file:
        for cont, result in enumerate(results):
            f_o = result.objective
            time = result.statistics['time'].total_seconds()
            file.write(f"{f_o} {time} {instancia_I[cont-1]} {instancia_J[cont-1]} {(cont+1)}\n")

def generate_data(range_for):
    global flag_error
    for i in range(range_for):
        cont = 0
        threads = []
        size = len(INSTANCIAS)
        for rango_bodegas, rango_tiendas in INSTANCIAS:
            cont += 1
            threads.append(threading.Thread(target=create_instance, args=(rango_bodegas,rango_tiendas,cont)))
            threads[cont-1].start()
            
        for i in range(size):
            threads[i].join()

        cont = 0
        threads = []

        for i in range(size):
            cont +=1
            modelo = f"modelo_minizinc{cont}.mzn"
            threads.append(threading.Thread(target=execute_mzn, args=(modelo,cont)))
            threads[i].start()

        for i in range(size):
            if not flag_error:
                threads[i].join()
            else:
                break

        if not flag_error:
            write_data()
            print("Instancias creadas.")
        
        flag_error = False
