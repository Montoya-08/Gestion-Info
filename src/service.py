from validate import validar_id, validar_correo

registros = []
ids = set()

def crear_registro(id, nombre, correo):
    try:
        validar_id(id, ids)
        validar_correo(correo)

        registro = {
            "id": id,
            "nombre": nombre,
            "correo": correo
        }

        registros.append(registro)
        ids.add(id)

        return "Registro creado"

    except ValueError as e:
        return f"Error: {e}"


def listar_registros():
    return registros