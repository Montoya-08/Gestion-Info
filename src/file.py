from colorama import Fore, init
init(autoreset=True)
import json
import os

RUTA = "data/records.json"

def load_data():
    try:
        if not os.path.exists(RUTA):
            return []

        with open(RUTA, "r") as archivo:
            return json.load(archivo)
        
    except FileNotFoundError:
        print(Fore.RED + "Error: Archivo no encontrado")
        return []

    except json.JSONDecodeError:
        print(Fore.RED + "Error: El archivo está dañado")
        return []

    except Exception as e:
        print(Fore.RED + f"Error inesperado: {e}")
        return []


def save_data(data):
    try:
        with open(RUTA, "w") as archivo:
            json.dump(data, archivo, indent=4)
        print(Fore.GREEN + "Datos guardados correctamente")

    except Exception as e:
        print(Fore.RED + f"Error al guardar: {e}")