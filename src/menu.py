from colorama import Fore, Style, init
import service
from file import load_data, save_data

init(autoreset=True)

def mostrar_menu():
    print(Fore.MAGENTA + "\n===== MENÚ =====")
    print("1. Crear registro")
    print("2. Listar registros")
    print("3. Buscar registro")
    print("4. Actualizar registro")
    print("5. Eliminar registro")
    print("6. Salir")


def ejecutar_menu():
    data = load_data()
    service.initialize_data(data)

    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                id = int(input("Ingrese ID: "))
                nombre = input("Ingrese nombre: ")
                correo = input("Ingrese correo: ")

                resultado = service.new_register(id, nombre, correo)
                print(resultado)

                if "Registro creado" in resultado:
                    save_data(service.registros)

            elif opcion == 2:
                print(Fore.MAGENTA + "\nRegistros:")
                service.list_records()

            elif opcion == 3:
                id = int(input("Ingrese ID a buscar: "))
                resultado = service.search_record(id)
                print(resultado)

            elif opcion == 4:
                id = int(input("ID a actualizar: "))
                print("Deje vacío si no desea cambiar el dato")
                nombre = input("Nuevo nombre: ")
                correo = input("Nuevo correo: ")

                resultado = service.update_record(id, nombre, correo)
                print(resultado)

                if "actualizado" in resultado:
                    save_data(service.registros)

            elif opcion == 5:
                id = int(input("ID a eliminar: "))
                resultado = service.delete_record(id)
                print(resultado)

                if "eliminado" in resultado:
                    save_data(service.registros)

            elif opcion == 6:
                print(Fore.GREEN + "Saliendo...")
                break

            else:
                print(Fore.RED + "Opción inválida")

        except ValueError:
            print(Fore.RED + "Error: Ingrese un número válido")