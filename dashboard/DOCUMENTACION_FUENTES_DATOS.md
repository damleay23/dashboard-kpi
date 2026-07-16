# Documentación de Fuentes de Datos - Dashboard KPI v2.9

## Resumen Ejecutivo

El dashboard utiliza datos del archivo CSV `historia_proforma_reporte.csv` que contiene 436,889 registros con información de cotizaciones, vendedores y almacenes.

---

## Tabla de Columnas del CSV `historia_proforma_reporte.csv`

| # | Columna | Tipo | Usado | Descripción |
|---|---------|------|------|-------------|
| 1 | `id` | int | ❌ | ID único del registro |
| 2 | `id_almacen` | int | ⚠️ EXISTE PERO NO SE USA | ID numérico del almacén (19, 42, 8, etc.) |
| 3 | `nombre_almacen` | string | ✅ | Nombre del almacén (ALM. JUAN TANCA MARENGO) |
| 4 | `cotizacion` | string | ✅ | ID de cotización (19-6988, FEV11383) |
| 5 | `id_asesor` | int | ❌ | ID del vendedor (no se usa, se usa nombre) |
| 6 | `nombre_vendedor` | string | ✅ | Nombre del vendedor/asesor |
| 7 | `ced_cliente` | string | ❌ | Cédula del cliente |
| 8 | `fecha_creacion_cliente` | datetime | ✅ | Fecha de creación (YYYY-MM-DD HH:MM:SS) |
| 9 | `fecha` | datetime | ✅ (ordenamiento) | Última actualización |
| 10 | `cotizacion_relacionada` | string | ❌ | Cotización relacionada |
| 11 | `motivo_relacion` | string | ❌ | Motivo de relación |
| 12 | `origen_negociacion` | string | ✅ | Canal: Llamada, Visita Almacen, Digitales, Externo |
| 13 | `cliente_compartido` | string | ❌ | Si es cliente compartido |
| 14 | `estado_cliente` | string | ❌ | Estado del cliente |
| 15 | `visita_almacen` | string | ❌ | Indicador de visita |
| 16 | `motivo_cliente` | string | ❌ | Motivo del cliente |
| 17 | `fecha_seguimiento` | datetime | ❌ | Fecha de seguimiento |
| 18 | `valor_factura` | float | ❌ | Valor de la factura |
| 19 | `cotizacion_recorrido` | string | ❌ | Cotización de recorrido |
| 20 | `observacion` | string | ❌ | Observaciones |
| 21 | `nombre_cliente` | string | ❌ | Nombre del cliente |
| 22 | `ultimo_registro` | float | ✅ | 1.0=final, 0.0=intermedio |
| 23 | `temperatura` | string | ❌ | Temperatura (Tibio, etc.) |
| 24 | `id_cliente_proforma` | string | ❌ | ID del cliente en Proforma |
| 25 | `numero_factura` | string | ✅ CRÍTICO | Número de factura (determina VENTA REAL) |
| 26 | `nombre_factura` | string | ❌ | Nombre de la factura |
| 27 | `idCotizacion` | string | ❌ | Otro ID de cotización |
| 28 | `donde_conocio` | string | ❌ | Dónde conoció al cliente |

---

## Mapeo de Datos Utilizados en el Dashboard

### 1. **ID ASESOR / NOMBRE VENDEDOR**
```
CSV Campo: nombre_vendedor (columna 6)
Ejemplos: "JANNETH LUNA", "Alejandro Garcia", "Belén Morales"
Uso en Dashboard:
  • Filtro de Asesor
  • Agrupación de datos
  • Métricas por vendedor
En datos.js: campo 'nombre_vendedor'
```

### 2. **ID ALMACÉN** ⚠️ IMPORTANTE
```
CSV Campo: id_almacen (columna 2)
Ejemplos: 19, 42, 8, 74, 80, 82, etc.
Estado: NO SE ESTÁ USANDO ACTUALMENTE - SOLO EXISTE EN CSV
Alternativa Usada: nombre_almacen (columna 3)

⚠️ RECOMENDACIÓN: Para diferenciar almacenes de forma única e inequívoca,
   se debería agregar id_almacen a datos.js en lugar de solo nombre_almacen
   
Estructura sugerida en datos.js:
  "almacen_id": 19
  "nombre_almacen": "ALM. JUAN TANCA MARENGO"
```

### 3. **NOMBRE ALMACÉN**
```
CSV Campo: nombre_almacen (columna 3)
Ejemplos: "ALM. JUAN TANCA MARENGO", "ALM. ORDOÑEZ LASSO", "ALM.GUAY.DICENTRO"
Uso en Dashboard:
  • Mostrar en matriz de canales
  • Filtro de almacén
  • Agrupación por almacén
Normalización:
  • "ALM.JUAN TANCA MARENGO" → "ALM. JUAN TANCA MARENGO" (agregar espacio)
En datos.js: campo 'nombre_almacen'
```

### 4. **COTIZACIÓN (ID ÚNICO)**
```
CSV Campo: cotizacion (columna 4)
Ejemplos: "19-6988", "19-7857", "FEV11383"
Uso en Dashboard:
  • DEDUPLICACIÓN PRINCIPAL (keep='last' en pandas)
  • Identificar cotizaciones únicas
Lógica de Ferias y Eventos:
  • Si cotizacion comienza con "FEV" → es de Ferias y Eventos
  • Ejemplo: "FEV11383", "FEV11384", etc.
En datos.js: NO se almacena explícitamente (solo se usó en deduplicación)
```

### 5. **ORIGEN NEGOCIACIÓN (CANAL DE CAPTURA)**
```
CSV Campo: origen_negociacion (columna 12)
Valores Únicos en CSV:
  • "Llamada"
  • "Visita Almacen"
  • "Digitales"
  • "Externo"
  • "Neo"
  • "Interno"
  • "- Origen del Cliente -"

Normalización Aplicada:
  • "Neo" → "Digitales"
  • "Interno" → "Visita Almacen"
  • "Externo" → "Visita Obra"
  
Categorías Finales en Dashboard:
  1. "Visita Almacen" = Cotizaciones hechas EN el almacén
  2. "Digitales" = Ingresos por formulario web
  3. "Llamada" = Ingresos por teléfono
  4. "Visita Obra" = Ingresos (visita del asesor al cliente)
  5. "Ferias y Eventos" = Detectado por prefix "FEV" en cotizacion
  
En datos.js: campo 'origen_negociacion' (normalizado)
```

### 6. **FECHA CREACIÓN (PARA EXTRAER AÑO Y MES)**
```
CSV Campo: fecha_creacion_cliente (columna 8)
Formato: "YYYY-MM-DD HH:MM:SS"
Ejemplo: "2022-03-25 05:00:00"

Procesamiento en Dashboard:
  • Extrae SOLO el AÑO → en datos.js campo 'año'
  • Extrae SOLO el MES → en datos.js campo 'mes'
  • Convierte a int: 2022, 1-12

Filtro Aplicado:
  • Mostrar SOLO años desde 2020 en adelante
  • Años anteriores a 2020 se cargan pero no se muestran en selector
  
En datos.js: 
  • 'año': int (2022, 2023, 2024, 2025, 2026)
  • 'mes': int (1-12, sin nombres)
  • 'mes_nombre': string (Enero, Febrero, etc.)
```

### 7. **FECHA ÚLTIMA ACTUALIZACIÓN (PARA ORDENAMIENTO)**
```
CSV Campo: fecha (columna 9)
Formato: "YYYY-MM-DD HH:MM:SS"
Uso EXCLUSIVO: Ordenamiento para keep='last' en deduplicación

Lógica:
  1. Se cargan todos los registros
  2. Se ordena por fecha de menor a mayor
  3. Se eliminan duplicados por cotizacion, MANTENIENDO EL ÚLTIMO
  → Esto asegura tomar el estado más reciente de cada cotización

En datos.js: NO se almacena (solo se usa en proceso)
```

### 8. **NÚMERO FACTURA** ⚠️ CRÍTICO
```
CSV Campo: numero_factura (columna 25)
Formato: string o NULL
Ejemplos: "001-001-000001234", "001-002-000005678", o vacío/NULL

USO CRÍTICO: DETERMINA SI ES UNA VENTA REAL

Lógica de Ventas Reales:
  Una cotización es VENDIDA solo si:
    ✅ numero_factura ≠ NULL AND
    ✅ numero_factura ≠ "" AND
    ✅ ultimo_registro = 1.0
  
  Si solo cumple ultimo_registro=1.0 pero numero_factura es NULL
    → NO SE CUENTA COMO VENTA (es un dato falso positivo)

Estadísticas:
  • ~5.41% de registros tienen numero_factura válido (23,639)
  • ~94.59% tienen numero_factura NULL (413,250)
  • De 23,639 con numero_factura + ultimo_registro=1.0:
    → 10,648 son VENTAS REALES confirmadas

En datos.js: Se procesa a 'cotizaciones_vendidas' (binary: 0 o count)
```

### 9. **ÚLTIMO REGISTRO**
```
CSV Campo: ultimo_registro (columna 22)
Valores: 1.0 (registro final) o 0.0 (registro intermedio)

Lógica:
  • 0.0 = Registro intermedio/seguimiento (NOT final state)
  • 1.0 = Registro final (estado final de la cotización)

Uso con numero_factura:
  • Se combina con numero_factura para validar ventas
  • ultimo_registro=1.0 + numero_factura válido = VENTA

En datos.js: Se procesa a binario 'es_vendida' (0 o 1)
```

### 10. **TOTALES CALCULADOS (NO del CSV directo)**
```
Estos campos NO existen en CSV, se CALCULAN:

'total_cotizaciones':
  = COUNT de registros agrupados por (asesor, mes, origen, almacén)
  = Número total de ingresos/cotizaciones en ese grupo
  
'cotizaciones_vendidas':
  = COUNT de registros donde es_vendida=1 en ese grupo
  = Número de ventas reales en ese grupo
  
'tasa_cierre':
  = (cotizaciones_vendidas / total_cotizaciones) * 100
  = Porcentaje de cierre/conversión
  
'mes_nombre':
  = Traducción de mes (1 → "Enero", 2 → "Febrero", etc.)
```

---

## Flujo de Datos: Entrada → Procesamiento → Dashboard

```
┌─────────────────────────────────────────────┐
│ historia_proforma_reporte.csv               │
│ (436,889 registros)                         │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ PASO 1: DEDUPLICACIÓN                       │
│ • Ordena por fecha                          │
│ • Elimina duplicados por 'cotizacion'       │
│ • Mantiene ÚLTIMO registro (keep='last')    │
│ Resultado: 64,447 cotizaciones únicas       │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ PASO 2: NORMALIZACIÓN                       │
│ • Neo → Digitales                           │
│ • Interno → Visita Almacen                  │
│ • Externo → Visita Obra                     │
│ • Detecta Ferias (prefijo FEV)              │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ PASO 3: EXTRACCIÓN DE FECHAS                │
│ • fecha_creacion_cliente → año + mes        │
│ • Valida que tenga fecha válida             │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ PASO 4: IDENTIFICACIÓN DE VENTAS            │
│ • numero_factura ≠ NULL AND                 │
│ • ultimo_registro = 1.0                     │
│ Resultado: 10,648 ventas reales             │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ PASO 5: AGRUPACIÓN Y CÁLCULO                │
│ Agrupa por: (asesor, mes, origen, almacén) │
│ Calcula: total, vendidas, tasa_cierre       │
│ Resultado: 13,199 registros                 │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ SALIDA: datos.js                            │
│ {                                           │
│   "resumen_general": {...},                 │
│   "filtros": {...},                         │
│   "por_asesor_mes_origen_almacen": [...]    │
│ }                                           │
└─────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ DASHBOARD (index.html)                      │
│ • Carga datos.js                            │
│ • Aplica filtros                            │
│ • Genera matrices, gráficos, métricas       │
└─────────────────────────────────────────────┘
```

---

## ⚠️ PROBLEMAS IDENTIFICADOS Y RECOMENDACIONES

### 1. **ID Almacén No Utilizado**
- **Problema**: Existe `id_almacen` en CSV pero se usa solo `nombre_almacen`
- **Riesgo**: Si hay variaciones en nombres, puede causar agrupación incorrecta
- **Solución**: Agregar `id_almacen` a `datos.js` como identificador único

### 2. **Ferias y Eventos no es un "Origen"**
- **Problema**: "Ferias y Eventos" se detecta por prefijo "FEV" en `cotizacion`, NO existe como `origen_negociacion`
- **Riesgo**: Inconsistencia en cómo se identifica
- **Solución**: Crear un campo `tipo_evento` para diferenciar (Ferias vs Normal)

### 3. **Campos Potencialmente Útiles No Almacenados**
- `ced_cliente`: Podría servir para deduplicar clientes
- `nombre_cliente`: Podría agregarse a reportes
- `temperatura`: Podría indicar "frio" clientes vs "calientes"

---

## Estructura Final en datos.js

```javascript
{
  "resumen_general": {
    "total_cotizaciones": 63608,
    "total_vendidas": 10648,
    "tasa_cierre": 16.74,
    "total_asesores": 84
  },
  "filtros": {
    "anos": [2002, 2003, ..., 2026],
    "asesores": ["ADRIANA CAROLINA LINO", "ALVARADO LOURDES", ...],
    "origenes": ["Digitales", "Llamada", "Visita Almacen", "Visita Obra"]
  },
  "por_asesor_mes_origen_almacen": [
    {
      "nombre_vendedor": "ADRIANA CAROLINA LINO",
      "año": 2002.0,
      "mes": 1.0,
      "origen_negociacion": "Llamada",
      "nombre_almacen": "ALM. JUAN TANCA MARENGO",
      "total_cotizaciones": 1,
      "cotizaciones_vendidas": 0,
      "tasa_cierre": 0.0,
      "mes_nombre": "Enero"
    },
    // ... más registros
  ]
}
```

---

## Información de Contacto / Preguntas

Para entender mejor un campo específico o validar datos:
1. Revisar el script: `DEDUPLICAR_COTIZACIONES_OPTIMIZADO.py`
2. Consultar el archivo CSV directamente: `KPI/csv_export/historia_proforma_reporte.csv`
3. Revisar estructura de regionales: `estructura_regionales_nuevos.json`
