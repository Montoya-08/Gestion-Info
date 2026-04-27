from colorama import Fore, init
init(autoreset=True)
def validar_id(id, ids_exixstentes):
    if id in ids_exixstentes:
        raise ValueError(Fore.RED + "El ID ya existe.")
    
def validar_correo(correo):
    if "@" not in correo:
        raise ValueError(Fore.RED + "Correo electrónico no válido.")    