# SALOS: Seismic Data Analysis System

Sistema de análisis y detección de eventos sísmicos diseñado para el procesamiento de señales en entornos de exploración espacial (Marte y la Luna). El software permite la identificación de terremotos mediante el análisis de umbrales de amplitud y la generación de representaciones gráficas automáticas.

## Descripción Técnica
El sistema procesa datos en formatos MiniSEED y CSV utilizando librerías científicas de Python para extraer segmentos significativos de actividad sísmica.

### Dependencias
* Python 3.x
* ObsPy
* NumPy
* Pandas
* Matplotlib

## Estructura del Proyecto

### 1. Script de Detección (Carpeta MARS)
Especializado en la identificación del inicio de eventos sísmicos.
* **Entradas:** Archivos MiniSEED y CSV con datos de amplitud.
* **Funcionalidad:** Identificación de picos mediante umbrales configurables (niveles amarillo y verde).
* **Salida:** Gráficos de la señal con áreas de detección resaltadas y marca de agua.

### 2. Análisis de Segmentos (Carpeta MOON)
Optimizado para el análisis de continuidad en señales sísmicas lunares.
* **Entradas:** Archivos MiniSEED y CSV.
* **Funcionalidad:** Identificación de segmentos continuos que representan la duración total de un evento.
* **Salida:** Visualización de bloques de datos que superan los umbrales específicos del entorno.

## Instrucciones de Uso

1. **Configuración:** Definir las rutas de los directorios de datos dentro de los scripts principales.
2. **Ejecución:**
   * Para análisis en Marte: Ejecutar el script dentro de la carpeta `/MARS`.
   * Para análisis en la Luna: Ejecutar el script dentro de la carpeta `/MOON`.
3. **Resultados:** Las visualizaciones generadas se almacenarán en el directorio de salida configurado para su revisión.

## Conclusión
SALOS proporciona una metodología estandarizada para la investigación sismológica fuera de la Tierra, facilitando el estudio de datos provenientes de misiones de exploración espacial.
