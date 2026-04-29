import sys
import os
sys.path.append(os.path.abspath("src"))

import service

def test_new_register():
    service.registros.clear()
    service.ids.clear()

    resultado = service.new_register(1, "Ana", "ana@mail.com")

    assert resultado == "Registro creado"
    assert len(service.registros) == 1

def test_id_duplicado():
    service.registros.clear()
    service.ids.clear()

    service.new_register(1, "Ana", "ana@mail.com")
    resultado = service.new_register(1, "Juan", "juan@mail.com")

    assert "Error" in resultado

def test_update_record():
    service.registros.clear()
    service.ids.clear()

    # Crear registro inicial
    service.new_register(1, "Ana", "ana@mail.com")

    # Actualizar nombre
    resultado = service.update_record(1, "Maria", "")

    assert resultado == "Registro actualizado"
    assert service.registros[0]["nombre"] == "Maria"
    assert service.registros[0]["correo"] == "ana@mail.com"
    
def test_delete_record():
    service.registros.clear()
    service.ids.clear()

    service.new_register(1, "Ana", "ana@mail.com")
    resultado = service.delete_record(1)

    assert resultado == "Registro eliminado"
    assert len(service.registros) == 0