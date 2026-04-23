from validate import validar_id, validar_correo

registros = []
ids = set()

def inicializar_datos(data):
    global registros, ids
    registros = data
    ids = {r["id"] for r in data}

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
    if not registros:
        print("No hay registros")
        return

    for r in registros:
        print(f"ID: {r['id']}")
        print(f"Nombre: {r['nombre']}")
        print(f"Correo: {r['correo']}")
        print("------------------")