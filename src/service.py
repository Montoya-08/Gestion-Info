from validate import validar_id, validar_correo

registros = []
ids = set()

def initialize_data(data):
    global registros, ids
    registros = data
    ids = {r["id"] for r in data}


def new_register(id: int, nombre: str, correo: str) -> str:
    """
    Crea un nuevo registro si el ID no existe.
    """
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


def search_record(id: int) -> dict | str:
    """
    Busca un registro por ID.
    """
    resultado = [r for r in registros if r["id"] == id]

    if not resultado:
        return "Error: Registro no encontrado"

    return resultado[0]


def update_record(id, nombre, correo):
    for r in registros:
        if r["id"] == id:

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


def new_register_dinamic(**kwargs):
    try:
        id = kwargs.get("id")
        nombre = kwargs.get("nombre")
        correo = kwargs.get("correo")

        return new_register(id, nombre, correo)

    except Exception as e:
        return f"Error: {e}"