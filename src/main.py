# print("Sistema listo")

# Crear un algoritmo que lea 3 números, los almacene en una lista y los ordene de mayor a menor.
# Manejo de funciones, listas, menú interactivo y manejo de errores.

"""
from colorama import Fore, Style, Back, init
init(autoreset=True) # Incializar colorama para restablecer colores automáticamente

print(Fore.BLUE + "======================================")
print(Back.CYAN + "===== Manejo de lista y errores ======")
print(Style.DIM + "============== By AMMT ===============")
print(Fore.BLUE + "======================================")

try:
    # Algoritmo a ejecutar
    print("Ingrese 3 números para ordenarlos de mayor a menor")
     
except ValueError: # TypeError, IndexError, ValueError
    print("Error: Ingrese un número válido")    
"""

from service import crear_registro, listar_registros

def main():
    while True:
        print("\n===== MENÚ =====")
        print("1. Crear registro")
        print("2. Listar registros")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id = int(input("Ingrese ID: "))
                nombre = input("Ingrese nombre: ")
                correo = input("Ingrese correo: ")

                print(crear_registro(id, nombre, correo))

            except ValueError:
                print("Error: ID inválido")

        elif opcion == "2":
            print("\nRegistros:")
            print(listar_registros())

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()