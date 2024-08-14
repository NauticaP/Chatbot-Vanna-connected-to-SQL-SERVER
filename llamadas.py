import streamlit as st
from vanna.remote import VannaDefault
import psycopg2
from psycopg2 import OperationalError
import vanna as vn
import pyodbc
import pandas as pd


# -------------------------------------------------
# Vamos a conectar a la base de datos de SQL Server
# ------------------------------------------------
db_name="SAWDB"
db_server="LMRP"
db_user='sa'
db_password=''

@st.cache_resource(ttl=3600)
def create_connection(db_name, db_server, db_user):
    connection = None
    try:
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={db_server};DATABASE={db_name};Trusted_Connection=yes;USER={db_user}'
        connection = pyodbc.connect(connection_string)
        print("Connection to SQL Server DB successful")
    except pyodbc.Error as e:
        print(f"The error '{e}' occurred")
    return connection


# ----------------------------------------------------------------------------------------------
# La función está decorada con @st.cache_resource(ttl=3600), 
# lo que significa que los resultados se cachearán durante una hora para mejorar el rendimiento.
# ----------------------------------------------------------------------------------------------
@st.cache_resource(ttl=3600)
def setup_vanna():
    api_key = '0cc56619601643e1b3831519a35abdc5'
    model = 'nauticap'

    # Crea la conexión a la base de datos usando pyodbc
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={db_server};DATABASE={db_name};Trusted_Connection=yes;USER={db_user}'
    vn = VannaDefault(api_key=api_key, model=model)
    vn.connect_to_mssql(odbc_conn_str=connection_string) # You can use the ODBC connection string here

    if True:
        
        return vn

    else:
        print("Failed to connect to SQL Server. Vanna aborted.")
        return None


# -------------------------------------------------------------------------------------------------------------------------------
# Genera preguntas de muestra utilizando la instancia de Vanna.
# Cachea los datos generados para optimizar el rendimiento, mostrando un spinner con el mensaje "Generating sample questions ..."
# -------------------------------------------------------------------------------------------------------------------------------
@st.cache_data(show_spinner="Generando preguntas de muestra...")
def generate_questions_cached():
    vn = setup_vanna()
    return vn.generate_questions()


# ---------------------------------------------------------------------------------------------
# Genera una consulta SQL a partir de una pregunta en lenguaje natural.
# También cachea los resultados, mostrando un spinner con el mensaje "Generating SQL query ..."
# ---------------------------------------------------------------------------------------------

@st.cache_data(show_spinner="Generando consulta SQL...")
def generate_sql_cached(question: str):
    vn = setup_vanna()
    return vn.generate_sql(question=question, allow_llm_to_see_data=True)
    

#---------------------------------------------------------------------------------------
#Verifica si una consulta SQL es válida.
#Cachea los resultados y muestra un spinner con el mensaje "Checking for valid SQL ...".
#---------------------------------------------------------------------------------------
@st.cache_data(show_spinner="Chequeando si la consulta SQL es válida...")
def is_sql_valid_cached(sql: str):
    vn = setup_vanna()
    return vn.is_sql_valid(sql=sql)

# ---------------------------------------------------------------------------------
#Ejecuta una consulta SQL y retorna los resultados.
#Cachea los resultados y muestra un spinner con el mensaje "Running SQL query ...".
# ---------------------------------------------------------------------------------
@st.cache_data(show_spinner="Corriendo la consulta SQL...")
def run_sql_cached(sql: str):
    vn = setup_vanna()
    return vn.run_sql(sql=sql)


# ---------------------------------------------------------------------------------------------------
#Determina si se debe generar un gráfico basado en los resultados de una consulta SQL.
#Cachea la decisión y muestra un spinner con el mensaje "Checking if we should generate a chart ...".
# ---------------------------------------------------------------------------------------------------
@st.cache_data(show_spinner="Chequeando si debemos generar un gráfico...")
def should_generate_chart_cached(question, sql, df):
    vn = setup_vanna()
    return vn.should_generate_chart(df=df)

# -------------------------------------------------------------------------------------------------------
#Genera el código necesario para crear un gráfico con Plotly basado en una consulta SQL y sus resultados.
#Cachea el código generado y muestra un spinner con el mensaje "Generating Plotly code ...".
# -------------------------------------------------------------------------------------------------------
@st.cache_data(show_spinner="Generando código Plotly...")
def generate_plotly_code_cached(question, sql, df):
    vn = setup_vanna()
    code = vn.generate_plotly_code(question=question, sql=sql, df=df)
    return code


# ----------------------------------------------------------------------------------
#Ejecuta el código de Plotly para generar un gráfico y retorna la figura resultante.
#Cachea la figura y muestra un spinner con el mensaje "Running Plotly code ...".
# ----------------------------------------------------------------------------------
@st.cache_data(show_spinner="Corriendo el código Plotly...")
def generate_plot_cached(code, df):
    vn = setup_vanna()
    return vn.get_plotly_figure(plotly_code=code, df=df)


#Genera preguntas de seguimiento basadas en la pregunta original, la consulta SQL y los resultados.
#Cachea las preguntas generadas y muestra un spinner con el mensaje "Generating followup questions ...".
#@st.cache_data(show_spinner="Generando preguntas de seguimiento...")
#def generate_followup_cached(question, sql, df):
#    vn = setup_vanna()
#    return vn.generate_followup_questions(question=question, sql=sql, df=df, num_questions=3, language="es")


# --------------------------------------------------------------------------------
#Genera un resumen basado en la pregunta original y los resultados de la consulta.
#Cachea el resumen y muestra un spinner con el mensaje "Generating summary ...".
# --------------------------------------------------------------------------------
@st.cache_data(show_spinner="Generando resumen...")
def generate_summary_cached(question, df):
    vn = setup_vanna()
    return vn.generate_summary(question=question, df=df)