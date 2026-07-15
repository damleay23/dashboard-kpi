# Filtros Regionales y de Almacén - Implementación Completada

## Resumen de Cambios

Se han agregado **dos nuevos filtros cascadeantes** al dashboard:

### 1. Filtro Regional
- **Ubicación**: Primera posición en la barra de filtros
- **Opciones**: 6 regiones
  - REGIÓN NORTE
  - REGIÓN CENTRO
  - REGIÓN SUR
  - REGIÓN COSTA
  - ADMINISTRACIÓN
  - OTROS
- **Comportamiento**: Al seleccionar una región, actualiza automáticamente el filtro de Almacén

### 2. Filtro Almacén (Cascadeante)
- **Ubicación**: Segunda posición en la barra de filtros
- **Comportamiento Dinámico**:
  - Cuando NO hay región seleccionada → Muestra todos los 20 almacenes
  - Cuando SÍ hay región seleccionada → Muestra SOLO los almacenes de esa región
- **Ejemplo**:
  - Región NORTE tiene 4 almacenes: ALM. ORDOÑEZ LASSO, ALM. QUITO, ALM. CUMBAYA, ALM. PLAZA PROYECTA
  - Región ADMINISTRACIÓN tiene 3 almacenes: ALM. FABRICA DURAMAS, DURAMAS CIA LTDA, ALM. MALL DEL RIO

### 3. Filtro Asesor (Mejorado)
- Ahora también es cascadeante
- Cuando SÍ hay región Y/O almacén seleccionado → Muestra SOLO asesores de ese almacén
- Mantiene la búsqueda autocomplete existente

## Orden de Filtros (Nuevo)
1. **Regional** (nuevo)
2. **Almacén** (nuevo)
3. **Año**
4. **Mes**
5. **Asesor**
6. **Origen**

## Datos de Estructura

La estructura de regiones y almacenes se carga desde `estructura_regiones.json` que contiene:

```
REGIÓN NORTE (4 almacenes, 52 asesores)
├── ALM. ORDOÑEZ LASSO (32 asesores)
├── ALM. QUITO (45 asesores)
├── ALM. CUMBAYA (38 asesores)
└── ALM. PLAZA PROYECTA (20 asesores)

REGIÓN CENTRO (3 almacenes, 50 asesores)
├── ALM. AMBATO (38 asesores)
├── BODEGA SANGOLQUI (34 asesores)
└── ALM. MISCELANEOS (4 asesores)

REGIÓN SUR (3 almacenes, 39 asesores)
├── ALM. CUENCA REMIGIO (17 asesores)
├── ALM. MANTA (23 asesores)
└── ALM. EL CARACOL (6 asesores)

REGIÓN COSTA (3 almacenes, 38 asesores)
├── ALM.GUAY.DICENTRO (24 asesores)
├── ALM.JUAN TANCA MARENGO (37 asesores)
└── ALM.GUAYAQUIL (3 asesores)

ADMINISTRACIÓN (3 almacenes, 35 asesores)
├── ALM. FABRICA DURAMAS (27 asesores)
├── DURAMAS CIA LTDA (21 asesores)
└── ALM. MALL DEL RIO (4 asesores)

OTROS (3 almacenes, 23 asesores)
├── DIGITAL (10 asesores)
├── EVENTOS (15 asesores)
└── RECORRIDO (2 asesores)
```

## Cambios Técnicos

### Archivos Modificados
1. **dashboard.html**
   - Agregados 2 nuevos `<select>` para Regional y Almacén
   - Agregadas funciones `cargarEstructuraRegiones()`, `actualizarAlmacenes()`, `actualizarAsesores()`
   - Actualizada función `actualizarDatos()` para aplicar filtros regionales
   - Actualizado `limpiarFiltros()` para limpiar nuevos filtros

2. **index.html**
   - Cambios idénticos a dashboard.html (sincronizados)

### Nuevas Funciones JavaScript
- `cargarEstructuraRegiones()` - Carga estructura_regiones.json
- `actualizarAlmacenes()` - Actualiza opciones del filtro Almacén según Region
- `actualizarAsesores()` - Actualiza lista de asesores según Region/Almacén
- Lógica de cascada en `actualizarDatos()` para filtrar por región/almacén

### Archivo de Datos
- `estructura_regiones.json` - Mapeo completo de Region → Almacen → [Asesores]

## Funcionalidades Preservadas
✓ KPIs dinámicos (se actualizan con todos los filtros)
✓ Gráficos (se actualizan dinámico)
✓ Tabla de datos (se filtra correctamente)
✓ Export a CSV
✓ Autocomplete de asesores
✓ Todos los 436,889 registros disponibles
✓ Design profesional Power BI

## Testing
- ✓ Filtro Regional funciona correctamente
- ✓ Filtro Almacén cascadea según Region seleccionada
- ✓ Filtro Asesor cascadea según Almacén seleccionado
- ✓ KPIs se actualizan dinámicamente
- ✓ Botón "Limpiar" limpia todos los 6 filtros
- ✓ Combinación de filtros funciona correctamente

## URLs
- Local: `http://localhost:8000/dashboard.html`
- Vercel: `https://dashboard-kpi-mu.vercel.app/`
