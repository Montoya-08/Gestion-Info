## Ejecucuión:

## Módulo 0:
1. Abre el archivo .py que deseas correr (En este caso main.py)
2. Opciónes:
- Presiona el botón ▶️ para correr el programa dentro del archivo .py
- Usar la terminal: 
Terminal
New Terminal 
cd src
python main.py

## Módulo 5:
## Gestión de Información
Aplicación en Python que permite gestionar registros con operaciones CRUD, persistencia en JSON y exportación a CSV usando pandas.

## Requisitos
- Python 3

## Instalación
Instalar dependencias:
pip install -r requirements.txt
py -m pipi install pandas
                                                                                                                                                               
## Ejecución
Ejecutar el programa desde la raíz del proyecto:
python src/main.py

## Notas
- Los datos se guardan en `data/records.json`
- El reporte se genera en `data/reporte.csv`

## Módulo 6
## Ejecución de pruebas

- Antes de ejecutar las pruebas, asegúrate de tener instalada la dependencia `pytest`: pip install pytest
- Luego ejecuta: python -m pytest tests/

### Resultado esperado

collected X items
...
X passed

Esto indica que todas las pruebas se ejecutaron correctamente.