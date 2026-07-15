# Guía de Uso - Nuevos Filtros Regional y Almacén

## 🎯 Descripción General

El dashboard ahora cuenta con **2 nuevos filtros cascadeantes** que te permiten filtrar datos por ubicación geográfica de forma intuitiva.

## 📍 Los 6 Nuevos Filtros (Ubicación)

### Orden en la Interfaz:
```
[Regional ▼] [Almacén ▼] [Año ▼] [Mes ▼] [Asesor 🔍] [Origen ▼] [Limpiar] [Exportar CSV]
```

## 🗺️ Opciones de Filtro Regional

| Regional | Almacenes | Asesores | Cotizaciones |
|----------|-----------|----------|--------------|
| REGIÓN NORTE | 4 | 52 | 207,162 |
| REGIÓN CENTRO | 3 | 50 | 99,432 |
| REGIÓN SUR | 3 | 39 | 33,347 |
| REGIÓN COSTA | 3 | 38 | 68,654 |
| ADMINISTRACIÓN | 3 | 35 | 26,869 |
| OTROS | 3 | 23 | 1,402 |
| **TODOS** | **20** | **68** | **436,889** |

## 🏪 Almacenes por Región

### REGIÓN NORTE (4 almacenes)
- ALM. ORDOÑEZ LASSO
- ALM. QUITO
- ALM. CUMBAYA
- ALM. PLAZA PROYECTA

### REGIÓN CENTRO (3 almacenes)
- ALM. AMBATO
- BODEGA SANGOLQUI
- ALM. MISCELANEOS

### REGIÓN SUR (3 almacenes)
- ALM. CUENCA REMIGIO
- ALM. MANTA
- ALM. EL CARACOL

### REGIÓN COSTA (3 almacenes)
- ALM.GUAY.DICENTRO
- ALM.JUAN TANCA MARENGO
- ALM.GUAYAQUIL

### ADMINISTRACIÓN (3 almacenes)
- ALM. FABRICA DURAMAS
- DURAMAS CIA LTDA
- ALM. MALL DEL RIO

### OTROS (3 almacenes)
- DIGITAL
- EVENTOS
- RECORRIDO

## 💡 Ejemplos de Uso

### Ejemplo 1: Ver solo REGIÓN NORTE

**Pasos:**
1. Click en filtro "Regional"
2. Seleccionar "REGIÓN NORTE"
3. El filtro "Almacén" se actualiza automáticamente

**Resultado:**
- Almacén muestra: ALM. ORDOÑEZ LASSO, ALM. QUITO, ALM. CUMBAYA, ALM. PLAZA PROYECTA
- Asesor muestra: 52 asesores de esa región
- KPIs se actualizan: ~207,162 cotizaciones
- Gráficos se actualizan en tiempo real

### Ejemplo 2: Filtrar por Almacén Específico

**Pasos:**
1. Click en "Regional" → Seleccionar "REGIÓN NORTE"
2. Click en "Almacén" → Seleccionar "ALM. QUITO"
3. Los asesores se actualizan automáticamente

**Resultado:**
- Solo muestra datos del ALM. QUITO
- Asesor lista solo: ~45 asesores de ALM. QUITO
- KPIs reflejan solo cotizaciones de ese almacén

### Ejemplo 3: Combinar Filtros Regional + Temporal

**Pasos:**
1. Regional: "REGIÓN CENTRO"
2. Almacén: "ALM. AMBATO"
3. Año: "2023"
4. Mes: "Enero"

**Resultado:**
- Muestra SOLO: Cotizaciones de ALM. AMBATO, en Enero 2023
- KPIs actualizados para esa combinación
- Gráficos muestran datos filtrados

### Ejemplo 4: Buscar por Asesor en Ubicación

**Pasos:**
1. Regional: "REGIÓN NORTE"
2. Almacén: (sin seleccionar)
3. Asesor: Escribir "Jazmina" y seleccionar

**Resultado:**
- Muestra: Cotizaciones de Jazmina en almacenes de REGIÓN NORTE
- Autocomplete funciona con asesores disponibles

### Ejemplo 5: Limpiar Todo

**Pasos:**
1. Click en botón "Limpiar"

**Resultado:**
- Se limpia: Regional, Almacén, Año, Mes, Asesor, Origen
- Vuelve a mostrar: Todos los 436,889 registros
- KPIs vuelven a los totales globales

## 🔄 Flujo de Cascada

La cascada funciona así:

```
1. Selecciona REGIÓN
   ↓
   → Almacén se ACTUALIZA (solo almacenes de esa región)

2. Selecciona ALMACÉN
   ↓
   → Asesor se ACTUALIZA (solo asesores de ese almacén)

3. Los datos se FILTRAN automáticamente
   → KPIs cambian
   → Gráficos se rediseñan
   → Tabla se actualiza
```

## 🎯 Casos de Uso Comunes

### Caso 1: Analizar REGIÓN NORTE en 2024
- Regional: REGIÓN NORTE
- Año: 2024
- Resultado: 207,162 cotizaciones filtradas a período 2024

### Caso 2: Performance por Almacén
- Ir almacén por almacén
- Observar tasas de cierre diferentes
- Comparar entre regiones

### Caso 3: Asesor en múltiples ubicaciones
- Seleccionar asesor (ej: "Jazmina Santamaría")
- Ver en qué almacenes trabaja
- Comparar su performance por ubicación

### Caso 4: Evaluar Origen por Región
- Regional: Una región
- Origen: Específico (ej: "Llamada")
- Ver efectividad de ese canal por región

## 📊 Impacto en KPIs

Los 4 KPIs se actualizan automáticamente:

| KPI | Sin Filtro | Con Regional NORTE | Con ALM. QUITO |
|-----|-----------|-------------------|-----------------|
| Total Cotizaciones | 436,889 | ~207,162 | ~72,069 |
| Vendidas | 31,087 | ~10,000 | ~4,011 |
| Tasa Cierre | 7.12% | ~4.8% | ~5.57% |
| Asesores | 68 | 52 | 45 |

## 🖱️ Controles Principales

### Filtro Regional
- **Ubicación**: Primer filtro de la barra
- **Tipo**: Dropdown select
- **Opciones**: 7 (6 regiones + Todos)
- **Efecto**: Actualiza dinámicamente Almacén

### Filtro Almacén
- **Ubicación**: Segundo filtro de la barra
- **Tipo**: Dropdown select
- **Opciones**: Dinámico (depende de Regional)
- **Efecto**: Actualiza dinámicamente Asesor

### Filtro Asesor (Mejorado)
- **Ubicación**: Quinto filtro de la barra
- **Tipo**: Autocomplete text input
- **Opciones**: Dinámicas (depende de Almacén)
- **Efecto**: Filtra data, oculta gráfico Top 10

### Botón Limpiar
- **Ubicación**: Lado derecho
- **Efecto**: Limpia TODOS los 6 filtros
- **Reset**: Vuelve a mostrar 436,889 registros

### Botón Exportar CSV
- **Ubicación**: Lado derecho (rojo)
- **Efecto**: Descarga data actual (con filtros aplicados)

## ⚠️ Notas Importantes

1. **Los filtros son ADITIVOS**
   - Regional NORTE + Mes Enero = Solo esa combinación
   - Combinación de múltiples filtros es permitida

2. **La cascada es AUTOMÁTICA**
   - No necesitas hacer clicks adicionales
   - Al seleccionar Regional, Almacén se actualiza al instante

3. **Puedes DESELECCIONAR**
   - Si cambias de idea, regresa a la opción "Todos"
   - Los otros filtros se actualizan nuevamente

4. **El Limpiar es COMPLETO**
   - Limpia todos los 6 filtros simultáneamente
   - Una acción, 6 filtros reset

5. **Mobile-Responsive**
   - Funciona en desktop, tablet, móvil
   - Los filtros se adaptan al tamaño de pantalla

## 🎓 Tips Prácticos

✓ **Empezar por arriba**: Región → Almacén → Asesor  
✓ **Usar después**: Año → Mes → Origen  
✓ **Comparar**: Cambiar solo 1 filtro para ver diferencias  
✓ **Exportar**: Click en "Exportar CSV" cuando tengas el filtro que quieres  
✓ **Limpiar**: Si no estás seguro, click "Limpiar" para empezar de nuevo

## 🔄 Casos de Multiples Ubicaciones

Algunos asesores trabajan en múltiples almacenes/regiones:

**Ejemplo: Jazmina Santamaría**
- Aparece en: 13 almacenes diferentes
- Regiones: 5 regiones distintas
- Total cotizaciones: ~36,361
- Tasa cierre: ~10.66%

Puedes ver su actividad:
1. Por región individual
2. Por almacén individual
3. Total consolidado (sin filtros)

---

**Última actualización**: Julio 14, 2026  
**Dashboard**: https://dashboard-kpi-mu.vercel.app/
