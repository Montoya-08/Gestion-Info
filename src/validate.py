def validar_id(id, ids_exixstentes):
    if id in ids_exixstentes:
        raise ValueError("El ID ya existe.")
    
def validar_correo(correo):
    if "@" not in correo:
        raise ValueError("Correo electrónico no válido.")    