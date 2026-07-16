#!/usr/bin/env python3
"""
Documentación de las fuentes de datos del Dashboard KPI
"""

import pandas as pd

CSV_PATH = r'KPI\csv_export\historia_proforma_reporte.csv'

print("=" * 80)
print("DOCUMENTACIÓN DE FUENTES DE DATOS - DASHBOARD KPI v2.9")
print("=" * 80)

# Leer el CSV
df = pd.read_csv(CSV_PATH, encoding='utf-8', low_memory=False, nrows=1)

print("\n=== COLUMNAS DEL CSV 'historia_proforma_reporte.csv' ===")
print(f"Total de columnas: {len(df.columns)}\n")
for i, col in enumerate(df.columns):
    print(f"{i+1:2d}. {col}")

# Leer algunos registros para ver qué se está usando
print("\n\n=== DATOS DE EJEMPLO (primer registro) ===")
df_ejemplo = pd.read_csv(CSV_PATH, encoding='utf-8', low_memory=False, nrows=1)

campos_clave = [
    'id_almacen',
    'nombre_almacen', 
    'cotizacion',
    'nombre_vendedor',
    'origen_negociacion',
    'fecha_creacion_cliente',
    'fecha',
    'numero_factura',
    'ultimo_registro'
]

print("\nCampos clave utilizados en el dashboard:\n")
for campo in campos_clave:
    if campo in df_ejemplo.columns:
        valor = df_ejemplo[campo].iloc[0]
        print(f"  ✓ {campo}")
        print(f"      Valor: {valor}")
        print(f"      Tipo: {df_ejemplo[campo].dtype}")
    else:
        print(f"  ✗ {campo} - NO ENCONTRADO")

print("\n\n=== MAPEO DE DATOS EN EL DASHBOARD ===\n")

mapeo = """
FUENTE DE DATOS: CSV 'historia_proforma_reporte.csv'

1. ID ASESOR / NOMBRE VENDEDOR
   ├─ Campo CSV: 'nombre_vendedor'
   ├─ Ejemplo: "JANNETH LUNA", "Alejandro Garcia"
   ├─ Uso: Filtro de Asesor, agrupación de datos
   └─ En datos.js: campo 'nombre_vendedor'

2. ID ALMACÉN
   ├─ Campo CSV: 'id_almacen'
   ├─ Ejemplo: 19, 42, 8, 74, etc.
   ├─ Uso: Identificar cada almacén de forma única
   └─ Nota: No se estaba usando, solo se usaba 'nombre_almacen'

3. NOMBRE ALMACÉN
   ├─ Campo CSV: 'nombre_almacen'
   ├─ Ejemplo: "ALM. JUAN TANCA MARENGO", "ALM. ORDOÑEZ LASSO"
   ├─ Uso: Mostrar nombre del almacén en la matriz
   ├─ Normalización: Se mapean variantes (ALM.JUAN -> ALM. JUAN)
   └─ En datos.js: campo 'nombre_almacen'

4. COTIZACION (ID)
   ├─ Campo CSV: 'cotizacion'
   ├─ Ejemplo: "19-6988", "19-7857", "FEV11383"
   ├─ Uso: Identificar cada cotización de forma única
   ├─ Lógica: Se deduplica por este campo (keep='last')
   ├─ Ferias/Eventos: Las que empiezan con "FEV"
   └─ En datos.js: NO se incluye explícitamente, pero se usa en deduplicación

5. ORIGEN NEGOCIACIÓN
   ├─ Campo CSV: 'origen_negociacion'
   ├─ Valores únicos: "Llamada", "Visita Almacen", "Digitales", "Externo", "Neo", "Interno"
   ├─ Normalización:
   │   ├─ "Neo" → "Digitales"
   │   ├─ "Interno" → "Visita Almacen"
   │   └─ "Externo" → "Visita Obra"
   ├─ Identificación Ferias: Se detecta por prefijo "FEV" en cotizacion, NO por origen
   └─ En datos.js: campo 'origen_negociacion'

6. FECHA CREACIÓN
   ├─ Campo CSV: 'fecha_creacion_cliente'
   ├─ Formato: YYYY-MM-DD HH:MM:SS
   ├─ Uso: Extraer AÑO y MES para agrupación
   ├─ Filtro: Solo años desde 2020 en adelante
   └─ En datos.js: Se extrae año ('año') y mes ('mes')

7. FECHA ÚLTIMA ACTUALIZACIÓN
   ├─ Campo CSV: 'fecha' (también llamada fecha_cierre)
   ├─ Formato: YYYY-MM-DD HH:MM:SS
   ├─ Uso: Ordenamiento para keep='last' en deduplicación
   └─ En datos.js: No se almacena directamente

8. NÚMERO FACTURA
   ├─ Campo CSV: 'numero_factura'
   ├─ Uso: CRÍTICO - Determina si es VENTA REAL
   ├─ Lógica: Una venta es válida solo si:
   │   ├─ numero_factura ≠ NULL/vacío
   │   ├─ AND ultimo_registro = 1.0
   ├─ En datos.js: Se procesa a 'cotizaciones_vendidas'
   └─ Nota: 94.59% de registros tienen numero_factura = NULL

9. ÚLTIMO REGISTRO
   ├─ Campo CSV: 'ultimo_registro'
   ├─ Valores: 1.0 (final) o 0.0 (intermedio)
   ├─ Uso: Junto con numero_factura determina ventas
   └─ En datos.js: Se procesa a 'es_vendida'

10. TOTALES CALCULADOS (no del CSV directo)
    ├─ 'total_cotizaciones': COUNT de cotizaciones agrupadas por asesor-mes-origen-almacén
    ├─ 'cotizaciones_vendidas': COUNT de vendidas (con numero_factura)
    ├─ 'tasa_cierre': (vendidas / total) * 100
    └─ 'mes_nombre': Traducción de mes a nombre en español
"""

print(mapeo)

print("\n\n=== IMPORTANTE: CAMPOS NO DOCUMENTADOS EN datos.js ===\n")
no_usados = """
Estos campos del CSV existen pero NO se almacenan en datos.js:
  • id_almacen: Solo existe como id, no se usa (se usa nombre_almacen)
  • cotizacion: Se usa solo para deduplicación, no se almacena
  • fecha: Se usa solo para ordenamiento, no se almacena
  • ultimo_registro: Se procesa a binario 'es_vendida'
  • numero_factura: Se usa solo para validación, no se almacena
  
Recomendación: Si necesitas usar id_almacen, debe agregarse a datos.js durante la generación.
"""
print(no_usados)
