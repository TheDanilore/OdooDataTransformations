import pandas as pd
import logging
import os

# Configuración de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Rutas a los archivos
archivo_original = "Productos/Productos.xlsx"
plantilla_odoo = "Productos/product_template.xlsx"
archivo_transformado = "Productos/productos_transformados.xlsx"
try:
    # Leer los archivos Excel
    df_original = pd.read_excel(archivo_original, skiprows=4)  # Saltar las primeras 4 filas que contienen encabezados innecesarios
    df_plantilla = pd.read_excel(plantilla_odoo)
    logging.info(f"Archivos leídos correctamente: {archivo_original} y {plantilla_odoo}")
except FileNotFoundError as e:
    logging.error(f"Error: No se encontró el archivo. {e}")
    raise
except Exception as e:
    logging.error(f"Error al leer los archivos: {e}")
    raise

# Imprimir los nombres de las columnas del archivo original para depuración
logging.info(f"Columnas en el archivo original: {df_original.columns.tolist()}")

# Renombrar las columnas del archivo original para que coincidan con los nombres esperados
df_original.columns = [
    'Creado', 'Nombre', 'Descripción', 'SKU', 'Código', 'Variante', 'Tags', 'Ropa',
    'Ropa Laboral', 'Bordados', 'Bebes', 'Almacén', 'Canal', 'Cuenta',
    'Stock', 'Stock virtual', 'Stock Disponible', 'Coste', 'Precio compra',
    'Valor coste', 'Valor venta', 'Subtotal', 'IVA', 'Retención', 'Rec. de eq.', 'Impuestos','Total'
]


# Definir el mapeo de campos
mapeo_campos = {
    'External ID': '',
    'Name': 'Nombre',  # Nombre del producto
    'Product Type':'',
    'Internal Reference':'',
    'Barcode':'',
    'Sales Price':'Valor venta',
    'Cost':'Precio compra',
    'Weight':'',
    'Sales Description':'Descripción',
}

# Crear un nuevo DataFrame para el archivo transformado
df_transformado = pd.DataFrame(columns=df_plantilla.columns)

# Transformar los datos según el mapeo de campos
for campo_odoo, campo_original in mapeo_campos.items():
    if campo_original in df_original.columns:
        df_transformado[campo_odoo] = df_original[campo_original]
        logging.info(f"Campo {campo_original} mapeado a {campo_odoo} correctamente.")
    else:
        logging.warning(f"Campo {campo_original} no encontrado en el archivo original.")

# Validar que todos los campos necesarios estén presentes
campos_requeridos = ['Name']
for campo in campos_requeridos:
    if campo not in df_transformado.columns or df_transformado[campo].isnull().all():
        logging.error(f"Campo requerido {campo} no está presente o está vacío en el archivo transformado.")
        raise ValueError(f"Campo requerido {campo} no está presente o está vacío en el archivo transformado.")

# Verificar si existe el archivo antes de guardarlo
if os.path.exists(archivo_transformado):
    os.remove(archivo_transformado)

try:
    # Guardar el archivo transformado
    df_transformado.to_excel(archivo_transformado, index=False)
    logging.info(f"Archivo transformado guardado correctamente en: {archivo_transformado}")
except Exception as e:
    logging.error(f"Error al guardar el archivo transformado: {e}")
    raise

print(f"Archivo transformado guardado en: {archivo_transformado}")
