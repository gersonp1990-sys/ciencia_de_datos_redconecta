import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Iniciando procesamiento de datos en una sola ejecución...")
ruta_dataset = 'dataset_set_D_telecomunicaciones.csv'
if ruta_dataset.endswith('.csv'):
    df = pd.read_csv(ruta_dataset, sep=';', encoding='latin1')
else:
    df = pd.read_excel(ruta_dataset)
num_cols = ['trafico_datos_gb', 'latencia_ms', 'tiempo_resolucion_hr']
for col in num_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
if 'fecha_registro' in df.columns:
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
cols_soporte = [
    'fecha_registro', 'region', 'tipo_servicio', 
    'incidencias_reportadas', 'tickets_soporte', 'tiempo_resolucion_hr'
]
df_soporte = df[cols_soporte].sort_values(by='fecha_registro')
df_soporte.to_excel('reporte_soporte_tecnico.xlsx', index=False)
cols_clientes = [
    'fecha_registro', 'tipo_servicio', 
    'clientes_afectados', 'latencia_ms', 'cumplimiento_sla'
]
df_clientes = df[cols_clientes].sort_values(by='fecha_registro')
df_clientes.to_excel('reporte_experiencia_clientes.xlsx', index=False)
print("-> Reportes Excel generados exitosamente: 'reporte_soporte_tecnico.xlsx' y 'reporte_experiencia_clientes.xlsx'.")
df_kpis = df.groupby(['region', 'tipo_servicio']).agg(
    cumplimiento_sla_pct=('cumplimiento_sla', lambda x: (x == 'Cumple').mean() * 100),
    tiempo_resolucion_prom=('tiempo_resolucion_hr', 'mean'),
    clientes_afectados_total=('clientes_afectados', 'sum')
).reset_index()
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(15, 11))
fig.suptitle('Dashboard Exploratorio de Operaciones - RedConecta Telecom S.A.', fontsize=16, fontweight='bold', y=0.98)
sns.barplot(data=df_kpis, x='region', y='cumplimiento_sla_pct', hue='tipo_servicio', ax=axes[0, 0], palette='Blues_d')
axes[0, 0].set_title('1. % Cumplimiento de SLA por Región y Servicio', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('% Cumplimiento SLA')
axes[0, 0].set_ylim(0, 100)
sns.barplot(data=df_kpis, x='region', y='tiempo_resolucion_prom', hue='tipo_servicio', ax=axes[0, 1], palette='Oranges_d')
axes[0, 1].set_title('2. Tiempo Promedio de Resolución (Horas) por Región', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Tiempo Resolución (Horas)')
sns.scatterplot(data=df, x='trafico_datos_gb', y='latencia_ms', hue='tipo_servicio', style='region', s=70, alpha=0.8, ax=axes[1, 0], palette='Set2')
axes[1, 0].set_title('3. Tráfico de Datos (GB) vs Latencia (ms)', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Tráfico de Datos (GB)')
axes[1, 0].set_ylabel('Latencia (ms)')
sns.barplot(data=df_kpis, x='region', y='clientes_afectados_total', hue='tipo_servicio', ax=axes[1, 1], palette='Reds_d')
axes[1, 1].set_title('4. Total Clientes Afectados por Región y Servicio', fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Clientes Afectados (Total)')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('dashboard_redconecta.png', dpi=300)
print("-> Imagen 'dashboard_redconecta.png' guardada con éxito.")
print("¡Abriendo ventana con el dashboard...!")
plt.show()
print("¡Proceso finalizado correctamente!")