# RESPUESTA DIRECTA: ¿DE DÓNDE SACO CADA DATO?

## Pregunta: "De donde estas tomando los datos, de donde sacas los id del asesor, los almacenes, los origenes, las fechas"

---

## RESPUESTA COMPLETA

### 1️⃣ **ID ASESOR / NOMBRE DEL VENDEDOR**

**¿De dónde?: CSV Column 6: `nombre_vendedor`**

```
CSV → historia_proforma_reporte.csv
     └─ Columna 6: nombre_vendedor
        ├─ Ejemplos: "JANNETH LUNA"
        ├─ Ejemplos: "Alejandro Garcia"
        ├─ Ejemplos: "Belén Morales"
        └─ Tipo: string (texto)

En datos.js:
  └─ Campo: "nombre_vendedor"
```

⚠️ **NOTA**: Existe un `id_asesor` (columna 5) pero NO se está usando
→ Se debería usar para identificar asesores de forma única sin depender del nombre

---

### 2️⃣ **ID ALMACÉN**

**¿De dónde?: CSV Column 2: `id_almacen` (pero NO se usa actualmente)**

```
CSV → historia_proforma_reporte.csv
     └─ Columna 2: id_almacen
        ├─ Ejemplos: 19, 42, 8, 74, 80, 82
        ├─ Tipo: integer (número)
        └─ Estado: ❌ NO SE ESTÁ USANDO

Se usa en su lugar:
  └─ Columna 3: nombre_almacen
     ├─ Ejemplos: "ALM. JUAN TANCA MARENGO"
     ├─ Ejemplos: "ALM. ORDOÑEZ LASSO"
     ├─ Tipo: string (texto)
     └─ En datos.js: "nombre_almacen"

En datos.js:
  └─ Campo: "nombre_almacen"

⚠️ PROBLEMA: Usar solo el nombre puede causar agrupación incorrecta
           si hay variantes de nombre para el mismo almacén
```

---

### 3️⃣ **ORIGEN / CANAL DE CAPTURA**

**¿De dónde?: CSV Column 12: `origen_negociacion`**

```
CSV → historia_proforma_reporte.csv
     └─ Columna 12: origen_negociacion
        ├─ Valores originales:
        │  ├─ "Llamada"
        │  ├─ "Visita Almacen"
        │  ├─ "Digitales"
        │  ├─ "Neo"
        │  ├─ "Interno"
        │  ├─ "Externo"
        │  └─ "- Origen del Cliente -"
        │
        ├─ NORMALIZACIÓN aplicada:
        │  ├─ "Neo" → "Digitales"
        │  ├─ "Interno" → "Visita Almacen"
        │  └─ "Externo" → "Visita Obra"
        │
        └─ "Ferias y Eventos":
           ├─ NO viene de origen_negociacion
           ├─ Se DETECTA por: prefijo "FEV" en columna 4 (cotizacion)
           └─ Ejemplos: "FEV11383", "FEV11384"

En datos.js:
  └─ Campo: "origen_negociacion" (después de normalizar)
     ├─ "Digitales"
     ├─ "Llamada"
     ├─ "Visita Almacen"
     ├─ "Visita Obra"
     └─ "Ferias y Eventos" (cuando cotizacion empieza con FEV)
```

---

### 4️⃣ **FECHAS: AÑO Y MES**

**¿De dónde?: CSV Column 8: `fecha_creacion_cliente`**

```
CSV → historia_proforma_reporte.csv
     └─ Columna 8: fecha_creacion_cliente
        ├─ Formato: "YYYY-MM-DD HH:MM:SS"
        ├─ Ejemplo: "2022-03-25 05:00:00"
        └─ Tipo: datetime (fecha y hora)

PROCESAMIENTO:
  1. Extrae el AÑO (2022) → campo "año"
  2. Extrae el MES (3) → campo "mes"
  3. Convierte a int: año=2022, mes=3
  4. Traduce mes a nombre: 3 → "Marzo"

FILTRO APLICADO:
  • Se cargan TODOS los años (2002-2026)
  • Pero en el filtro del dashboard SOLO se muestran 2020+
  • Los años 2002-2019 están cargados pero ocultos

En datos.js:
  ├─ Campo: "año" (int: 2002-2026)
  ├─ Campo: "mes" (int: 1-12)
  └─ Campo: "mes_nombre" (string: "Enero", "Febrero", etc.)
```

---

### 5️⃣ **COTIZACIONES (ID ÚNICO)**

**¿De dónde?: CSV Column 4: `cotizacion`**

```
CSV → historia_proforma_reporte.csv
     └─ Columna 4: cotizacion
        ├─ Ejemplos: "19-6988"
        ├─ Ejemplos: "19-7857"
        ├─ Ejemplos: "FEV11383"
        └─ Tipo: string o int

USO:
  • Es la CLAVE de deduplicación
  • Se eliminan duplicados por esta columna
  • Se mantiene el ÚLTIMO registro (keep='last')
  • Resultado: 64,447 cotizaciones únicas de 436,889 registros

DETECCIÓN DE FERIAS:
  • SI cotizacion comienza con "FEV" → es Feria
  • Ejemplo: "FEV11383" → Feria
  • Ejemplo: "19-6988" → Normal

En datos.js:
  └─ NO se almacena explícitamente
     (se usó solo para deduplicación)
```

---

### 6️⃣ **NÚMERO DE FACTURA (VALIDA VENTAS REALES)**

**¿De dónde?: CSV Column 25: `numero_factura`**

```
CSV → historia_proforma_reporte.csv
     └─ Columna 25: numero_factura
        ├─ Ejemplos: "001-001-000001234"
        ├─ O VACÍO/NULL: (No hay factura)
        └─ Tipo: string

USO CRÍTICO:
  Una cotización es VENTA REAL SOLO SI:
    ✅ numero_factura ≠ NULL AND
    ✅ numero_factura ≠ "" AND
    ✅ ultimo_registro = 1.0

ESTADÍSTICAS:
  • Total registros: 436,889
  • Con numero_factura válido: 23,639 (5.41%)
  • Con numero_factura NULL: 413,250 (94.59%)
  • PERO: 87,745 tienen ultimo_registro=1.0 sin factura
    → Son FALSOS POSITIVOS (parecían ventas pero NO lo son)
  • VENTAS REALES: 10,648

En datos.js:
  └─ Se procesa a: "cotizaciones_vendidas" (0 o count)
```

---

### 7️⃣ **ÚLTIMO REGISTRO (INDICADOR DE ESTADO FINAL)**

**¿De dónde?: CSV Column 22: `ultimo_registro`**

```
CSV → historia_proforma_reporte.csv
     └─ Columna 22: ultimo_registro
        ├─ Valores: 1.0 o 0.0
        ├─ 1.0 = Registro final (estado final de cotización)
        ├─ 0.0 = Registro intermedio (seguimiento)
        └─ Tipo: float

USO:
  • Se combina CON numero_factura para validar ventas
  • Si ultimo_registro=1.0 pero numero_factura=NULL → NO es venta
  • Si numero_factura=válido + ultimo_registro=1.0 → ES venta

En datos.js:
  └─ Se procesa a: "es_vendida" (0 o 1)
```

---

### 8️⃣ **TOTALES Y CÁLCULOS (NO vienen del CSV directo)**

**¿De dónde?: SE CALCULAN en el script**

```
Estos campos NO existen en el CSV, se GENERAN:

1. "total_cotizaciones"
   = COUNT de registros agrupados por (asesor, mes, origen, almacén)
   = Número total de ingresos/cotizaciones en ese grupo

2. "cotizaciones_vendidas"
   = COUNT de registros donde numero_factura ≠ NULL
      Y ultimo_registro = 1.0
   = Número de ventas reales en ese grupo

3. "tasa_cierre"
   = (cotizaciones_vendidas / total_cotizaciones) * 100
   = Porcentaje de conversión/cierre

4. "mes_nombre"
   = Traducción: 1 → "Enero", 2 → "Febrero", etc.
```

---

## RESUMEN EN UNA TABLA

| QUÉ | CSV COLUMNA | NOMBRE CAMPO | TIPO DATO | ESTADO |
|-----|-------------|--------------|-----------|--------|
| Nombre Asesor | 6 | nombre_vendedor | string | ✅ USADO |
| ID Almacén | 2 | id_almacen | int | ⚠️ NO USADO |
| Nombre Almacén | 3 | nombre_almacen | string | ✅ USADO |
| Origen/Canal | 12 | origen_negociacion | string | ✅ USADO |
| Cotización ID | 4 | cotizacion | string | ✅ DEDUP |
| Año | 8 | fecha_creacion_cliente (extrae año) | int | ✅ USADO |
| Mes | 8 | fecha_creacion_cliente (extrae mes) | int | ✅ USADO |
| Número Factura | 25 | numero_factura | string | ✅ CRÍTICO |
| Último Registro | 22 | ultimo_registro | float | ✅ CRÍTICO |
| Ferias/Eventos | 4 | cotizacion (prefijo FEV) | string | ✅ DETECTA |

---

## ⚠️ PROBLEMAS IDENTIFICADOS

### 1. ID Almacén NO se está usando
- **Existe**: Column 2 `id_almacen` con valores 19, 42, 8, etc.
- **Se usa en su lugar**: nombre_almacen (strings)
- **Problema**: Si hay variantes de nombre, no diferencia bien
- **Recomendación**: Agregar id_almacen a datos.js

### 2. Ferias y Eventos NO es un "Origen"
- **Se detecta**: Por prefijo "FEV" en cotizacion (column 4)
- **NO existe**: Como valor en origen_negociacion (column 12)
- **Problema**: Inconsistencia en categorización
- **Recomendación**: Crear campo `tipo_evento` o verificar si todas las ferias están marcadas con FEV

### 3. 94.59% de registros SIN número de factura
- **5.41%**: Tienen numero_factura válido
- **94.59%**: Tienen numero_factura NULL
- **Resultado**: Solo 10,648 de 436,889 son ventas reales (2.43%)
- **Implicación**: La tasa de cierre 16.74% es CORRECTA (10,648 / 63,608)

---

## PROCESO COMPLETO EN CÓDIGO

```python
1. Lee CSV:
   df = pd.read_csv('historia_proforma_reporte.csv')

2. Deduplica:
   df = df.drop_duplicates(subset=['cotizacion'], keep='last')

3. Extrae datos:
   año = df['fecha_creacion_cliente'].dt.year
   mes = df['fecha_creacion_cliente'].dt.month
   es_venta = (df['numero_factura'].notna()) & (df['ultimo_registro'] == 1.0)

4. Normaliza origen:
   if origen == 'Neo': origen = 'Digitales'
   if origen == 'Interno': origen = 'Visita Almacen'
   if origen == 'Externo': origen = 'Visita Obra'
   if cotizacion.startswith('FEV'): origen = 'Ferias y Eventos'

5. Agrupa:
   grupo = (nombre_vendedor, año, mes, origen, nombre_almacen)
   total_cot = count(grupo)
   total_vendidas = count(grupo where es_venta=1)
   tasa = (vendidas / total) * 100

6. Genera salida:
   datos.js con estructura: {resumen_general, filtros, por_asesor_mes_origen_almacen}
```

---

## CONCLUSIÓN

**De donde se saca todo:**

✅ **Del CSV `historia_proforma_reporte.csv`:**
- Nombre vendedor → Columna 6
- Nombre almacén → Columna 3  
- Origen → Columna 12 (+ detecta Ferias por Columna 4)
- Año/Mes → Columna 8
- Número factura → Columna 25 (para validar ventas)
- Último registro → Columna 22 (para validar ventas)

⚠️ **NO se usa pero EXISTE:**
- ID Almacén → Columna 2 (debería usarse)
- ID Asesor → Columna 5 (debería usarse)

🧮 **Se CALCULA:**
- Total cotizaciones, vendidas, tasa cierre
- Traducción de mes a nombre

