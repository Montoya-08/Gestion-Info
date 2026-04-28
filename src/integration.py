import pandas as pd
from colorama import Fore, init
init(autoreset=True)

RUTA_CSV = "data/reporte.csv"

def exportar(registros):
    try:
        if not registros:
            print(Fore.RED + "No hay datos para exportar")
            return

        df = pd.DataFrame(registros)
        df.to_csv(RUTA_CSV, index=False)

        print(Fore.GREEN + "Reporte exportado a CSV correctamente")

    except Exception as e:
        print(Fore.RED + f"Error al exportar: {e}")