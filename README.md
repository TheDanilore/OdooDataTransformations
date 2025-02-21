# Transformación de Datos para Odoo

Este repositorio contiene scripts en Python para la transformación de datos desde archivos Excel hacia un formato compatible con Odoo.

## 📂 Estructura del proyecto

```bash
Scripts/
│── ETL_Scripts_Odoo/
│   ├── transformar_odoo_productos.py  # Script para transformar productos
│   ├── productos_transformados.xlsx   # Salida del proceso
│   ├── Productos/                     # Carpeta con archivos de entrada
│       ├── Productos.xlsx
│       ├── product_template.xlsx
│── README.md
```

## 🚀 Requisitos
- Python 3.8+
- Pandas
- OpenPyXL (pip install pandas openpyxl)

## 🛠️ Uso

Ejecuta el script desde la terminal:

```bash
python transformar_odoo_productos.py
```

El script leerá los archivos de la carpeta Productos/, transformará los datos y generará un nuevo archivo productos_transformados.xlsx.

## 📋 Funcionalidades
- ✅ Lee archivos Excel y extrae datos relevantes.
- ✅ Mapea los datos según el formato requerido por Odoo.
- ✅ Valida la presencia de campos obligatorios.
- ✅ Guarda la salida en un nuevo archivo Excel.
