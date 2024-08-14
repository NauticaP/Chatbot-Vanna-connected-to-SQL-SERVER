# Chatbot con Vanna.AI conectado a SQL Server

Este proyecto consiste en un chatbot desarrollado con Streamlit y Vanna.AI que se conecta a una base de datos SQL Server. El chatbot puede responder preguntas en lenguaje natural, generar consultas SQL, ejecutar las consultas en la base de datos y mostrar los resultados, incluyendo gráficos generados con Plotly.

## Estructura del Proyecto

El proyecto está organizado en tres archivos principales:

### 1. `chatbot.py`
Este archivo es el punto de entrada de la aplicación Streamlit. Configura la interfaz de usuario y gestiona la interacción con el usuario a través del historial de mensajes. Cuando el usuario hace una pregunta, el chatbot:

- Genera una consulta SQL utilizando Vanna.AI.
- Ejecuta la consulta en la base de datos SQL Server.
- Muestra los resultados en forma de tabla.
- Genera y muestra gráficos si es aplicable.
- Ofrece un resumen basado en los resultados.

### 2. `llamadas.py`
Este archivo contiene todas las funciones auxiliares que permiten la interacción con Vanna.AI y la base de datos SQL Server:

- `create_connection`: Establece una conexión con la base de datos SQL Server.
- `setup_vanna`: Configura la instancia de Vanna.AI para su uso.
- `generate_sql_cached`: Genera una consulta SQL basada en una pregunta en lenguaje natural.
- `run_sql_cached`: Ejecuta una consulta SQL en la base de datos y retorna los resultados.
- `generate_plotly_code_cached`: Genera el código de Plotly para crear gráficos basados en los resultados de la consulta.
- `generate_plot_cached`: Genera y retorna la figura gráfica basada en el código de Plotly.
- `generate_summary_cached`: Genera un resumen de los resultados obtenidos.

### 3. `train.py`
Este archivo se utiliza para entrenar a Vanna.AI con los metadatos de la base de datos SQL Server:

- Conecta a la base de datos.
- Recupera información sobre las tablas y columnas.
- Genera sentencias DDL (Data Definition Language) para entrenar a Vanna.AI.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.8 o superior
- Streamlit
- Vanna.AI SDK
- pyodbc
- psycopg2
- pandas
- plotly

Puedes instalar las dependencias necesarias utilizando `pip`:

```bash
pip install streamlit vanna pyodbc psycopg2 pandas plotly
```

## Configuración
- Configuración de la Base de Datos: Asegúrate de actualizar las variables de conexión a la base de datos SQL Server en llamadas.py y train.py.

- Clave API de Vanna.AI: En el archivo llamadas.py, proporciona tu clave API de Vanna.AI y el modelo que deseas utilizar.

- Ejecución del Chatbot: Para ejecutar la aplicación, usa el siguiente comando.

```bash
streamlit run chatbot.py
```
Esto abrirá una ventana del navegador con la interfaz del chatbot, donde podrás hacer preguntas en lenguaje natural. El chatbot generará consultas SQL, ejecutará las consultas, mostrará los resultados y generará gráficos si es aplicable.

- Entrenamiento de Vanna.AI: Si deseas entrenar a Vanna.AI con los metadatos de tu base de datos, ejecuta el archivo train.py:

```bash
python train.py
```

## Características

- Interfaz amigable: Diseñado con Streamlit para una interacción sencilla.
- Generación de SQL: Convierte preguntas en lenguaje natural en consultas SQL.
- Conexión a SQL Server: Ejecuta las consultas en una base de datos SQL Server.
- Visualización de Datos: Muestra resultados en tablas y genera gráficos interactivos con Plotly.
- Resumen de Resultados: Ofrece un resumen textual de los resultados obtenidos.

## Contribuciones
Si deseas contribuir a este proyecto, siéntete libre de abrir un pull request o reportar problemas en la sección de issues.

