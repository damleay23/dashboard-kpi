// Vercel Edge Function to serve dashboard data
// This file serves the KPI data without loading the large datos.js file

export default function handler(req, res) {
  // Temporary mock data - will be replaced with actual data loading
  const datosTemporales = {
    resumen_general: {
      total_cotizaciones: 436889,
      total_vendidas: 31087,
      tasa_cierre: 7.12,
      total_asesores: 68
    },
    filtros: {
      anos: [2022, 2023, 2024],
      asesores: ["ARQ OLEAS EDUARDO", "ASESOR 2", "ASESOR 3"],
      origenes: ["- Origen del Cliente -", "Llamada", "Visita Almacen"]
    },
    por_asesor_mes_origen_almacen: []
  };

  res.setHeader('Content-Type', 'application/json');
  res.setHeader('Access-Control-Allow-Origin', '*');
  
  res.status(200).json(datosTemporales);
}
