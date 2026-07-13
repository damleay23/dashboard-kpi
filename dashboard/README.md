# Dashboard KPI - Análisis de Cotizaciones

Dashboard interactivo para análisis de cotizaciones por asesor, origen y almacén con tasa de cierre.

## Características

- 📊 3 gráficos interactivos (Total vs Vendidas, Por Origen, Top 10 Asesores)
- 🔍 Búsqueda y filtrado de asesores con autocomplete
- 📅 Filtros por: Año, Mes, Asesor, Origen
- 📈 Visualización de tasa de cierre
- 📥 Exportación de datos a CSV
- 🎯 436,889 cotizaciones analizadas

## Filtros Disponibles

- **Año**: Datos desde 2022 a 2024
- **Mes**: Enero a Diciembre
- **Asesor**: 68 asesores disponibles (búsqueda rápida)
- **Origen**: 8 categorías de origen de negociación

## Datos

- **Total de Cotizaciones**: 436,889
- **Cotizaciones Vendidas**: 31,087
- **Tasa General de Cierre**: 7.12%
- **Asesores**: 68

## Uso Local

```bash
python servidor.py
```

Luego abre: `http://localhost:8000/dashboard.html`

## Despliegue

Este proyecto está desplegado en Vercel y se actualiza automáticamente con cada push a main.

**Dashboard en línea**: [Accede aquí](https://dashboard-kpi.vercel.app/dashboard.html)

## Estructura de Datos

- `dashboard.html` - Interfaz principal
- `datos.js` - Datos agregados (3 MB)
- `autocomplete-asesor.js` - Funcionalidad de búsqueda
- `KPI/csv_export/historia_proforma_reporte_FINAL.csv` - Fuente de datos

## Autor

Creado para análisis de cotizaciones y KPI de ventas.
