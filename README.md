# 📡 Análisis Operacional y Calidad de Servicio — RedConecta Telecom S. A.

## 📌 1. Descripción del Proyecto
Este proyecto desarrolla una solución analítica integrada, modular y reproducible en Python para procesar el registro operacional de **RedConecta Telecom S. A.**, evaluando el desempeño de la red de telecomunicaciones en las regiones Norte, Centro y Sur.

El flujo de trabajo automatiza la ingesta y limpieza de datos, genera reportes estructurados en formato Excel orientados a las áreas de **Soporte Técnico** y **Experiencia de Clientes**, construye un **Dashboard Exploratorio** de cuatro cuadrantes para orientar decisiones basadas en evidencia, e integra un pipeline de cálculo estadístico avanzado con persistencia binaria mediante **Joblib**.

---

## 🎯 2. Objetivos del Proyecto

* **Objetivo General**: Evaluar la eficiencia operativa, la calidad de servicio y la variabilidad de métricas de red para respaldar decisiones estratégicas de inversión y optimización de recursos.
* **Objetivos Específicos**:
  1. **Procesamiento y Estandarización**: Limpiar y convertir de forma explícita las métricas de tráfico (GB), latencia (ms), tiempos de atención (hrs) y cumplimiento de SLA a partir del dataset operacional.
  2. **Generación de Salidas Diferenciadas**: Exportar reportes especializados en formato Excel adaptados a las necesidades operativas de Soporte Técnico y estratégicas de Experiencia de Clientes.
  3. **Visualización Integrada**: Construir un dashboard exploratorio multicuadrante para identificar patrones regionales, cuellos de botella e interrupciones del servicio.
  4. **Modularidad y Reproducibilidad**: Encapsular las funciones de cálculo en scripts reutilizables y garantizar la persistencia de KPIs para ejecuciones futuras mediante Joblib.
  5. **Control de Versiones y Documentación**: Publicar los entregables en un repositorio centralizado en GitHub bajo la rama `main`, respaldado por documentación técnica en Markdown.

---

## 📁 3. Estructura y Componentes del Repositorio

```text
ciencia_de_datos_redconecta/
│
├── 📄 README.md                            <- Documentación técnica descriptiva en sintaxis Markdown
├── 📊 dataset_set_D_telecomunicaciones.csv  <- Registro operacional fuente (200 eventos)
├── 📜 soporteTecnico.py                    <- Script principal de ejecución inicial (Pregunta N° 3)
├── ⚙️ soporteTecnico_reutilizable.py       <- Pipeline analítico modular y parametrizado (Pregunta N° 4)
├── 💾 kpis_telecom.joblib                  <- Artefacto binario comprimido con KPIs persistidos (Joblib)
├── 🖼️ dashboard_redconecta.png             <- Visualización del Dashboard Exploratorio (300 DPI)
├── 📈 reporte_soporte_tecnico.xlsx         <- Reporte estructurado para el área de Soporte Técnico
└── 📈 reporte_experiencia_clientes.xlsx    <- Reporte estructurado para la gerencia de Experiencia

---

### 📑 Inventario de Entregables

| Archivo / Artefacto                   | Formato          | Área Destino / Uso   | Descripción Técnica                                       |
| :------------------------------------ | :--------------- | :------------------- | :-------------------------------------------------------- |
| `README.md`                           | Markdown         | General / Evaluación | Guía descriptiva del flujo, metodología y resultados.     |
| `dataset_set_D_telecomunicaciones.csv` | CSV              | Analítica de Datos   | Registro fuente con 200 eventos de red.                   |
| `soporteTecnico.py`                   | Python (`.py`)   | Pipeline Inicial     | Script ejecutable para el pipeline unificado inicial.     |
| `soporteTecnico_reutilizable.py`      | Python (`.py`)   | Pipeline Modular     | Script parametrizado con funciones, NumPy y SciPy.        |
| `kpis_telecom.joblib`                 | Binario (`.joblib`)| Persistencia de Datos| Objeto comprimido para carga directa con Joblib.          |
| `dashboard_redconecta.png`            | PNG (300 DPI)    | Gerencia Operativa   | Visualización comparativa regional y por servicio.        |
| `reporte_soporte_tecnico.xlsx`        | Excel (`.xlsx`)  | Soporte Técnico      | Mapeo de tickets, incidencias y tiempos de resolución.    |
| `reporte_experiencia_clientes.xlsx`   | Excel (`.xlsx`)  | Experiencia Clientes | Métricas de latencia, usuarios afectados y SLA.           |

---

🛠️ 4. Requisitos e Instalación
Para ejecutar este proyecto en tu entorno local, asegúrate de contar con Python 3.10+ y las siguientes librerías instaladas:
pip install pandas numpy scipy openpyxl joblib matplotlib

---

🚀 Modo de Ejecución
Para correr el pipeline modular y regenerar todos los entregables, ejecuta en tu terminal:
python soporteTecnico_reutilizable.py

---
👤 Autor
Gerson Peña — Proyecto de Ciencia de Datos (IACC, 2026).
Repositorio: https://github.com/gersonp1990-sys/ciencia_de_datos_redconecta

---
