# ==============================================================================
# ARCHIVO: soporteTecnico_reutilizable.py
# PROYECTO: RedConecta Telecom S. A. - Pipeline Analítico Modular y Reutilizable
# LIBRERÍAS: os, pandas, numpy, scipy, openpyxl, joblib
# ==============================================================================

import os
import pandas as pd
import numpy as np
from scipy import stats
from joblib import dump, load

# ------------------------------------------------------------------------------
# MÓDULO 1: Ingesta y Limpieza de Datos (Función Modular)
# ------------------------------------------------------------------------------
def cargar_y_limpiar_datos(ruta_csv):
    """
    Carga el dataset operativo y estandariza forzadamente los formatos numéricos y de fechas.
    """
    df = pd.read_csv(ruta_csv, sep=';', encoding='latin1')
    
    # Conversión explícita y forzada de decimales con coma (,) a tipo flotante (float)
    cols_float = ['trafico_datos_gb', 'latencia_ms', 'tiempo_resolucion_hr']
    for col in cols_float:
        if col in df.columns:
            s_clean = df[col].astype(str).str.replace(',', '.', regex=False)
            df[col] = pd.to_numeric(s_clean, errors='coerce')
            
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
    return df

# ------------------------------------------------------------------------------
# MÓDULO 2: Cálculo Estadístico Avanzado (NumPy + SciPy)
# ------------------------------------------------------------------------------
def calcular_kpis_avanzados(df):
    """
    Calcula métricas descriptivas e intervalos de confianza (95%) con NumPy y SciPy.
    """
    # Conversión directa a arreglos NumPy asegurando tipos numéricos limpios
    latencias = pd.to_numeric(df['latencia_ms'], errors='coerce').dropna().values
    tiempos = pd.to_numeric(df['tiempo_resolucion_hr'], errors='coerce').dropna().values
    
    # Cómputo numérico de promedios y desviaciones con NumPy
    lat_mean, lat_std = np.mean(latencias), np.std(latencias, ddof=1)
    t_mean, t_std = np.mean(tiempos), np.std(tiempos, ddof=1)
    
    # Intervalos de confianza al 95% con SciPy
    ic_lat = stats.t.interval(0.95, df=len(latencias)-1, loc=lat_mean, scale=stats.sem(latencias))
    ic_t = stats.t.interval(0.95, df=len(tiempos)-1, loc=t_mean, scale=stats.sem(tiempos))
    
    kpis = {
        'latencia_prom_ms': round(float(lat_mean), 2),
        'ic95_latencia': (round(float(ic_lat[0]), 2), round(float(ic_lat[1]), 2)),
        'tiempo_resolucion_prom_hr': round(float(t_mean), 2),
        'ic95_tiempo': (round(float(ic_t[0]), 2), round(float(ic_t[1]), 2))
    }
    return kpis

# ------------------------------------------------------------------------------
# MÓDULO 3: Exportación de Reportes en Excel
# ------------------------------------------------------------------------------
def exportar_reportes_excel(df, carpeta_salida="."):
    """
    Genera las salidas diferenciadas en formato Excel para las áreas correspondientes.
    """
    ruta_soporte = os.path.join(carpeta_salida, 'reporte_soporte_tecnico.xlsx')
    ruta_experiencia = os.path.join(carpeta_salida, 'reporte_experiencia_clientes.xlsx')
    
    # Reporte para Soporte Técnico
    df_soporte = df[['fecha_registro', 'region', 'tipo_servicio', 
                     'incidencias_reportadas', 'tickets_soporte', 'tiempo_resolucion_hr']]
    df_soporte.to_excel(ruta_soporte, index=False)
    
    # Reporte para Experiencia de Clientes
    df_experiencia = df[['fecha_registro', 'tipo_servicio', 
                         'clientes_afectados', 'latencia_ms', 'cumplimiento_sla']]
    df_experiencia.to_excel(ruta_experiencia, index=False)
    
    print("[ÉXITO] Reportes en Excel generados correctamente.")

# ------------------------------------------------------------------------------
# MÓDULO 4: Persistencia de Artefactos (Joblib)
# ------------------------------------------------------------------------------
def guardar_persistencia_joblib(kpis, ruta_salida):
    """
    Guarda el diccionario de KPIs en un archivo binario comprimido (.joblib).
    """
    dump(kpis, ruta_salida)
    print(f"[ÉXITO] Artefacto persistido mediante Joblib en: '{ruta_salida}'")

# ------------------------------------------------------------------------------
# MÓDULO PRINCIPAL DE EJECUCIÓN (Pipeline Unificado)
# ------------------------------------------------------------------------------
def main():
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    nombre_csv = 'dataset_set_D_telecomunicaciones.csv'
    
    ruta_dataset = os.path.join(directorio_script, nombre_csv)
    if not os.path.exists(ruta_dataset):
        if os.path.exists(nombre_csv):
            ruta_dataset = nombre_csv
        else:
            print(f"[ERROR] No se encontró el archivo '{nombre_csv}' en la carpeta del script.")
            return

    print("=== INICIANDO PIPELINE ANALÍTICO REUTILIZABLE ===")
    
    # 1. Carga y Limpieza
    df = cargar_y_limpiar_datos(ruta_dataset)
    print(f"1. Dataset cargado: {len(df)} registros procesados exitosamente.")
    
    # 2. Cálculo Estadístico Avanzado (NumPy + SciPy)
    kpis = calcular_kpis_avanzados(df)
    print(f"2. KPIs Calculados con SciPy/NumPy:")
    print(f"   - Latencia Media: {kpis['latencia_prom_ms']} ms (IC 95%: {kpis['ic95_latencia']})")
    print(f"   - Tiempo Resolución Medio: {kpis['tiempo_resolucion_prom_hr']} hrs (IC 95%: {kpis['ic95_tiempo']})")
    
    # 3. Exportación a Excel
    exportar_reportes_excel(df, carpeta_salida=directorio_script)
    
    # 4. Persistencia con Joblib
    ruta_joblib = os.path.join(directorio_script, "kpis_telecom.joblib")
    guardar_persistencia_joblib(kpis, ruta_joblib)
    
    # 5. Verificación de lectura desde Joblib
    kpis_recuperados = load(ruta_joblib)
    print(f"[REUTILIZACIÓN] Verificación de lectura desde Joblib: Latencia = {kpis_recuperados['latencia_prom_ms']} ms")
    
    print("=== PIPELINE EJECUTADO CON ÉXITO ===")

if __name__ == '__main__':
    main()