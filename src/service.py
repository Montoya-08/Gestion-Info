from validate import validar_id, validar_correo

registros = []
ids = set()

def initialize_data(data):
    global registros, ids
    registros = data
    ids = {r["id"] for r in data}

def new_register(id, nombre, correo):
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

def list_records():
    if not registros:
        print("No hay registros")
        return

    for r in registros:
        print(f"ID: {r['id']}")
        print(f"Nombre: {r['nombre']}")
        print(f"Correo: {r['correo']}")
        print("------------------")

def search_record(id):
    resultado = [r for r in registros if r["id"] == id]

    if not resultado:
        return "Error: El ID no existe"

    return resultado[0]

def update_record(id, nombre, correo):
    for r in registros:
        if r["id"] == id:

            # ✔ Solo cambia si escribió algo
            if nombre.strip():
                r["nombre"] = nombre

            if correo.strip():
                validar_correo(correo)
                r["correo"] = correo

            return "Registro actualizado"

    return "Error: ID no existe"

def delete_record(id):
    global registros

    for r in registros:
        if r["id"] == id:
            registros.remove(r)
            ids.remove(id)
            return "Registro eliminado"

    return "Error: ID no existe"

def sort_by_name():
    return sorted(registros, key=lambda r: r["nombre"])