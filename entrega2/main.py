from config import *
from generateData import generate_data
from createGraphs import create_graphs

def main():
    flag_continue = True
    while flag_continue:
        print("0. Salir.\n1. Generar datos.\n2. Generar grafico con los datos obtenidos.\n")
        option = int(input("\nSelecciona una opcion: "))
        match(option):
            case 1:
                range_for = int(input("\nSelecciona cuantas veces deseas obtener datos: "))
                generate_data(range_for)
            case 2:
                create_graphs()
            case 0:
                flag_continue = False
            case _: 
                "\nOpcion incorrecta"

    return

if __name__ == '__main__':
    main()
