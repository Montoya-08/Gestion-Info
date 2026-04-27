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

from menu import ejecutar_menu

def main():
    ejecutar_menu()

if __name__ == "__main__":
    main()