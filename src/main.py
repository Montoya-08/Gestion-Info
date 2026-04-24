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

import service
from file import load_data, save_data

def main():
    data = load_data()
    service.initialize_data(data)

    while True:
        print("\n===== MENÚ =====")
        print("1. Crear registro")
        print("2. Listar registros")
        print("3. Buscar registro")
        print("4. Actualizar registro")
        print("5. Eliminar registro")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id = int(input("Ingrese ID: "))
                nombre = input("Ingrese nombre: ")
                correo = input("Ingrese correo: ")

                resultado = service.new_register(id, nombre, correo)
                print(resultado)

                if "Registro creado" in resultado:
                    save_data(service.registros)

            except ValueError:
                print("Error: El ID ya existe o es inválido")

        elif opcion == "2":
            print("\nRegistros:")
            service.list_records()

        elif opcion == "3":
            try:
                id = int(input("Ingrese ID a buscar: "))
                resultado = service.search_record(id)
                print(resultado)

            except ValueError:
                print("Error: ID inválido")

        elif opcion == "4":
            try:
                id = int(input("ID a actualizar: "))
                nombre = input("Nuevo nombre: ")
                correo = input("Nuevo correo: ")

                resultado = service.update_record(id, nombre, correo)
                print(resultado)

                if "actualizado" in resultado:
                    save_data(service.registros)

            except ValueError:
                print("Error: ID inválido")

        elif opcion == "5":
            try:
                id = int(input("ID a eliminar: "))

                resultado = service.delete_record(id)
                print(resultado)

                if "eliminado" in resultado:
                    save_data(service.registros)

            except ValueError:
                print("Error: ID inválido")

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()